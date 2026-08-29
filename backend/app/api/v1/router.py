from fastapi import APIRouter
from app.authentication.router import router as auth_router
from app.users.router import router as users_router
from app.categories.router import router as categories_router
from app.products.router import router as products_router
from app.search.router import router as search_router
from app.cart.router import router as cart_router
from app.wishlist.router import router as wishlist_router
from app.coupons.router import router as coupons_router
from app.orders.router import router as orders_router
from app.payments.router import router as payments_router
from app.shipping.router import router as shipping_router
from app.reviews.router import router as reviews_router
from app.inventory.router import router as inventory_router
from app.vendors.router import router as vendors_router
from app.notifications.router import router as notifications_router
from app.admin.router import router as admin_router
from app.recommendations.router import router as recommendations_router
from app.analytics.router import router as analytics_router
from app.styling.router import router as styling_router

api_router = APIRouter()

# Core Authentication & Users
api_router.include_router(auth_router)
api_router.include_router(users_router)

# Fashion Catalog & Discovery
api_router.include_router(categories_router)
api_router.include_router(products_router)
api_router.include_router(search_router)

# Shopping Experience
api_router.include_router(cart_router)
api_router.include_router(wishlist_router)
api_router.include_router(coupons_router)

# Commerce Engine
api_router.include_router(orders_router)
api_router.include_router(payments_router)
api_router.include_router(shipping_router)
api_router.include_router(reviews_router)
api_router.include_router(inventory_router)

# Marketplace & Governance
api_router.include_router(vendors_router)
api_router.include_router(notifications_router)
api_router.include_router(admin_router)

# Fashion Intelligence, Styling & Recommendations
api_router.include_router(recommendations_router)
api_router.include_router(styling_router)

# Business Intelligence & Analytics
api_router.include_router(analytics_router)
