from typing import List, Tuple, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, func
from sqlalchemy.orm import selectinload

from app.core.exceptions import NotFoundException, BadRequestException
from app.core.events import event_bus, EventType
from app.users.models import User
from app.products.models import Product
from app.orders.models import Order, OrderItem, OrderStatus
from app.reviews.models import Review, ReviewImage, ReviewVote, FitFeedback
from app.reviews.schemas import ReviewCreate, ReviewSummaryOut


class ReviewService:
    @staticmethod
    async def create_review(db: AsyncSession, user: User, review_in: ReviewCreate) -> Review:
        # Check product
        prod_stmt = select(Product).where(Product.id == review_in.product_id)
        prod_res = await db.execute(prod_stmt)
        product = prod_res.scalar_one_or_none()
        if not product:
            raise NotFoundException("Product not found")

        # Check if verified purchase (User ordered this product and it was delivered)
        verified_stmt = (
            select(OrderItem)
            .join(Order, OrderItem.order_id == Order.id)
            .where(
                Order.user_id == user.id,
                OrderItem.product_id == review_in.product_id,
                Order.status == OrderStatus.DELIVERED
            )
        )
        verified_res = await db.execute(verified_stmt)
        is_verified = verified_res.scalar_one_or_none() is not None

        review = Review(
            product_id=review_in.product_id,
            user_id=user.id,
            order_id=review_in.order_id,
            rating=review_in.rating,
            title=review_in.title,
            comment=review_in.comment,
            fit_feedback=review_in.fit_feedback,
            quality_rating=review_in.quality_rating,
            is_verified_purchase=is_verified,
            is_approved=True
        )
        db.add(review)
        await db.flush()

        for idx, img_url in enumerate(review_in.images):
            img = ReviewImage(review_id=review.id, image_url=img_url, display_order=idx)
            db.add(img)

        # Recalculate product rating
        ratings_stmt = select(func.avg(Review.rating), func.count(Review.id)).where(
            Review.product_id == review_in.product_id,
            Review.is_approved == True
        )
        r_res = await db.execute(ratings_stmt)
        avg_rating, count = r_res.one()

        product.average_rating = round(float(avg_rating or review_in.rating), 1)
        product.review_count = int(count or 1)

        await db.commit()

        await event_bus.publish(
            EventType.REVIEW_CREATED,
            {"review_id": review.id, "product_id": review.product_id, "rating": review.rating}
        )

        return await ReviewService.get_by_id(db, review.id)

    @staticmethod
    async def get_by_id(db: AsyncSession, review_id: str) -> Review:
        stmt = select(Review).options(selectinload(Review.images)).where(Review.id == review_id)
        res = await db.execute(stmt)
        review = res.scalar_one_or_none()
        if not review:
            raise NotFoundException("Review not found")
        return review

    @staticmethod
    async def list_product_reviews(
        db: AsyncSession, product_id: str, page: int = 1, limit: int = 20
    ) -> Tuple[List[Review], int]:
        stmt = (
            select(Review)
            .options(selectinload(Review.images))
            .where(Review.product_id == product_id, Review.is_approved == True)
            .order_by(Review.helpful_votes.desc(), Review.created_at.desc())
        )
        count_stmt = select(func.count(Review.id)).where(Review.product_id == product_id, Review.is_approved == True)
        total_res = await db.execute(count_stmt)
        total = total_res.scalar() or 0

        offset = (page - 1) * limit
        stmt = stmt.offset(offset).limit(limit)
        res = await db.execute(stmt)
        return list(res.scalars().all()), total

    @staticmethod
    async def get_summary(db: AsyncSession, product_id: str) -> ReviewSummaryOut:
        stmt = select(Review).where(Review.product_id == product_id, Review.is_approved == True)
        res = await db.execute(stmt)
        reviews = list(res.scalars().all())

        if not reviews:
            return ReviewSummaryOut(
                average_rating=0.0,
                total_reviews=0,
                rating_breakdown={"5": 0, "4": 0, "3": 0, "2": 0, "1": 0},
                fit_feedback_breakdown={"RUNS_SMALL": 0, "TRUE_TO_SIZE": 0, "RUNS_LARGE": 0}
            )

        rating_counts = {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0}
        fit_counts = {"RUNS_SMALL": 0, "TRUE_TO_SIZE": 0, "RUNS_LARGE": 0}
        total_score = 0

        for r in reviews:
            total_score += r.rating
            r_key = str(r.rating)
            if r_key in rating_counts:
                rating_counts[r_key] += 1
            if r.fit_feedback.value in fit_counts:
                fit_counts[r.fit_feedback.value] += 1

        avg = round(total_score / len(reviews), 1)

        return ReviewSummaryOut(
            average_rating=avg,
            total_reviews=len(reviews),
            rating_breakdown=rating_counts,
            fit_feedback_breakdown=fit_counts
        )

    @staticmethod
    async def vote_helpful(db: AsyncSession, review_id: str, user_id: str, is_helpful: bool) -> None:
        review = await ReviewService.get_by_id(db, review_id)
        vote_stmt = select(ReviewVote).where(ReviewVote.review_id == review_id, ReviewVote.user_id == user_id)
        res = await db.execute(vote_stmt)
        vote = res.scalar_one_or_none()

        if not vote:
            vote = ReviewVote(review_id=review_id, user_id=user_id, is_helpful=is_helpful)
            db.add(vote)
            if is_helpful:
                review.helpful_votes += 1
        else:
            if vote.is_helpful != is_helpful:
                vote.is_helpful = is_helpful
                review.helpful_votes += 1 if is_helpful else -1

        await db.commit()
