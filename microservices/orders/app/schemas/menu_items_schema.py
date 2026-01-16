from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from uuid import UUID
from decimal import Decimal


class MenuItemBase(BaseModel):
    category_id: Optional[UUID] = None
    name: str = Field(..., max_length=255)
    description: Optional[str] = None
    price: Decimal = Field(..., ge=0, decimal_places=2)
    image_url: Optional[str] = Field(None, max_length=500)
    is_available: bool = True
    preparation_time: Optional[int] = Field(None, ge=0)


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    category_id: Optional[UUID] = None
    name: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    price: Optional[Decimal] = Field(None, ge=0, decimal_places=2)
    image_url: Optional[str] = Field(None, max_length=500)
    is_available: Optional[bool] = None
    preparation_time: Optional[int] = Field(None, ge=0)


class MenuItemInDB(MenuItemBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class MenuItem(MenuItemInDB):
    pass


class MenuItemWithCategory(MenuItem):
    category_name: Optional[str] = None