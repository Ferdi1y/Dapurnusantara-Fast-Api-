from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime
from uuid import UUID
from enum import Enum


class UserRole(str, Enum):
    customer = "customer"
    staff = "staff"
    admin = "admin"


class UserBase(BaseModel):
    email: EmailStr
    phone: Optional[str] = None
    full_name: str
    role: UserRole


class UserCreate(UserBase):
    password: str = Field(..., min_length=6)


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    full_name: Optional[str] = None
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None
    password: Optional[str] = Field(None, min_length=6)


class UserInDB(UserBase):
    id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class User(UserInDB):
    pass


class UserLogin(BaseModel):
    email: EmailStr
    password: str