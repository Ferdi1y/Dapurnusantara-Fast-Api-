from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from enum import Enum


class DiscountType(str, Enum):
    percentage = "percentage"
    fixed = "fixed"


class CouponBase(BaseModel):
    code: str = Field(..., max_length=50)
    description: Optional[str] = None
    discount_type: DiscountType
    discount_value: Decimal = Field(..., ge=0, decimal_places=2)
    min_purchase: Decimal = Field(default=0, ge=0, decimal_places=2)
    max_discount: Optional[Decimal] = Field(None, ge=0, decimal_places=2)
    usage_limit: Optional[int] = Field(None, ge=0)
    valid_from: Optional[datetime] = None
    valid_until: Optional[datetime] = None
    is_active: bool = True


class CouponCreate(CouponBase):
    pass


class CouponUpdate(BaseModel):
    code: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = None
    discount_type: Optional[DiscountType] = None
    discount_value: Optional[Decimal] = Field(None, ge=0, decimal_places=2)
    min_purchase: Optional[Decimal] = Field(None, ge=0, decimal_places=2)
    max_discount: Optional[Decimal] = Field(None, ge=0, decimal_places=2)
    usage_limit: Optional[int] = Field(None, ge=0)
    valid_from: Optional[datetime] = None
    valid_until: Optional[datetime] = None
    is_active: Optional[bool] = None


class CouponInDB(CouponBase):
    id: UUID
    used_count: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Coupon(CouponInDB):
    pass


class CouponValidation(BaseModel):
    is_valid: bool
    message: str
    discount_amount: Optional[Decimal] = None