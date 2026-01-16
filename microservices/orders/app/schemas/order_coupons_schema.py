from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from uuid import UUID
from decimal import Decimal


class OrderCouponBase(BaseModel):
    order_id: UUID
    coupon_id: UUID
    discount_amount: Decimal = Field(..., ge=0, decimal_places=2)


class OrderCouponCreate(OrderCouponBase):
    pass


class OrderCouponInDB(OrderCouponBase):
    id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class OrderCoupon(OrderCouponInDB):
    pass


class OrderCouponDetail(OrderCoupon):
    coupon_code: Optional[str] = None
    discount_type: Optional[str] = None