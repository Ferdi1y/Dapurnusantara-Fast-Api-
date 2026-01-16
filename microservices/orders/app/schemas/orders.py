from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from enum import Enum


class OrderType(str, Enum):
    dine_in = "dine_in"
    takeaway = "takeaway"
    delivery = "delivery"


class OrderStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    preparing = "preparing"
    ready = "ready"
    completed = "completed"
    cancelled = "cancelled"


class OrderItemBase(BaseModel):
    menu_item_id: UUID
    quantity: int = Field(..., ge=1)
    notes: Optional[str] = None


class OrderBase(BaseModel):
    order_type: OrderType
    table_number: Optional[str] = Field(None, max_length=20)
    delivery_address: Optional[str] = None
    notes: Optional[str] = None


class OrderCreate(OrderBase):
    items: List[OrderItemBase] = Field(..., min_length=1)
    coupon_code: Optional[str] = None


class OrderUpdate(BaseModel):
    status: Optional[OrderStatus] = None
    table_number: Optional[str] = Field(None, max_length=20)
    delivery_address: Optional[str] = None
    notes: Optional[str] = None


class OrderItemInDB(BaseModel):
    id: UUID
    order_id: UUID
    menu_item_id: Optional[UUID] = None
    quantity: int
    unit_price: Decimal
    subtotal: Decimal
    notes: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class OrderItemDetail(OrderItemInDB):
    menu_item_name: Optional[str] = None
    menu_item_image: Optional[str] = None


class OrderInDB(OrderBase):
    id: UUID
    user_id: Optional[UUID] = None
    order_number: str
    subtotal: Decimal
    tax: Decimal
    discount: Decimal
    delivery_fee: Decimal
    total_amount: Decimal
    status: OrderStatus
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Order(OrderInDB):
    pass


class OrderDetail(Order):
    items: List[OrderItemDetail] = []
    user_name: Optional[str] = None
    user_email: Optional[str] = None


class OrderSummary(BaseModel):
    id: UUID
    order_number: str
    order_type: OrderType
    status: OrderStatus
    total_amount: Decimal
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)