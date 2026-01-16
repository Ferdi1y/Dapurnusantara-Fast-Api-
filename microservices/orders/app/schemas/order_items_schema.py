from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from uuid import UUID
from decimal import Decimal


class OrderItemBase(BaseModel):
    menu_item_id: UUID
    quantity: int = Field(..., ge=1)
    notes: Optional[str] = None


class OrderItemCreate(OrderItemBase):
    order_id: UUID
    unit_price: Decimal = Field(..., ge=0, decimal_places=2)
    subtotal: Decimal = Field(..., ge=0, decimal_places=2)


class OrderItemUpdate(BaseModel):
    quantity: Optional[int] = Field(None, ge=1)
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


class OrderItem(OrderItemInDB):
    pass