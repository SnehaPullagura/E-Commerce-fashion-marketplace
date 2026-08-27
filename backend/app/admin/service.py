from typing import List, Dict, Any, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, func

from app.core.exceptions import NotFoundException
from app.users.models import User, UserRole
from app.vendors.models import VendorProfile, VendorStatus
from app.products.models import Product, ProductStatus
from app.orders.models import Order, SubOrder, OrderStatus, PaymentStatus
from app.admin.models import PlatformSetting
from app.admin.schemas import (
    PlatformSettingCreate,
    ModerateVendorRequest,
    ModerateProductRequest,
    AdminOverviewStats,
)


class AdminService:
    @staticmethod
    async def get_overview_stats(db: AsyncSession) -> AdminOverviewStats:
        # Users count
        u_stmt = select(func.count(User.id)).where(User.is_deleted == False)
        u_res = await db.execute(u_stmt)
        total_users = u_res.scalar() or 0

        # Vendors count
        v_stmt = select(func.count(VendorProfile.id)).where(VendorProfile.is_deleted == False)
        v_res = await db.execute(v_stmt)
        total_vendors = v_res.scalar() or 0

        # Pending vendors
        vp_stmt = select(func.count(VendorProfile.id)).where(VendorProfile.status == VendorStatus.PENDING)
        vp_res = await db.execute(vp_stmt)
        pending_vendors = vp_res.scalar() or 0

        # Products count
        p_stmt = select(func.count(Product.id)).where(Product.is_deleted == False)
        p_res = await db.execute(p_stmt)
        total_products = p_res.scalar() or 0

        # Orders & GMV
        o_stmt = select(func.count(Order.id), func.sum(Order.total_amount)).where(Order.payment_status == PaymentStatus.PAID)
        o_res = await db.execute(o_stmt)
        paid_orders_count, total_gmv = o_res.one()

        # Commissions sum
        comm_stmt = select(func.sum(SubOrder.commission_amount)).join(Order, SubOrder.order_id == Order.id).where(Order.payment_status == PaymentStatus.PAID)
        comm_res = await db.execute(comm_stmt)
        total_comm = comm_res.scalar() or 0.0

        return AdminOverviewStats(
            total_users=total_users,
            total_vendors=total_vendors,
            pending_vendors=pending_vendors,
            total_products=total_products,
            total_orders=paid_orders_count or 0,
            total_gmv=round(float(total_gmv or 0.0), 2),
            total_revenue_commission=round(float(total_comm or 0.0), 2)
        )

    @staticmethod
    async def moderate_vendor(
        db: AsyncSession, vendor_id: str, req: ModerateVendorRequest
    ) -> VendorProfile:
        stmt = select(VendorProfile).where(VendorProfile.id == vendor_id)
        res = await db.execute(stmt)
        vendor = res.scalar_one_or_none()
        if not vendor:
            raise NotFoundException("Vendor not found")

        vendor.status = req.status
        if req.commission_rate is not None:
            vendor.commission_rate = req.commission_rate

        await db.commit()
        await db.refresh(vendor)
        return vendor

    @staticmethod
    async def moderate_product(
        db: AsyncSession, product_id: str, req: ModerateProductRequest
    ) -> Product:
        stmt = select(Product).where(Product.id == product_id)
        res = await db.execute(stmt)
        product = res.scalar_one_or_none()
        if not product:
            raise NotFoundException("Product not found")

        product.status = req.status
        await db.commit()
        await db.refresh(product)
        return product

    @staticmethod
    async def set_setting(db: AsyncSession, req: PlatformSettingCreate) -> PlatformSetting:
        stmt = select(PlatformSetting).where(PlatformSetting.key == req.key.upper())
        res = await db.execute(stmt)
        setting = res.scalar_one_or_none()

        if not setting:
            setting = PlatformSetting(
                key=req.key.upper(),
                value=req.value,
                description=req.description,
                is_public=req.is_public
            )
            db.add(setting)
        else:
            setting.value = req.value
            if req.description:
                setting.description = req.description
            setting.is_public = req.is_public

        await db.commit()
        await db.refresh(setting)
        return setting
