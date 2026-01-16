from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict, Any
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from enum import Enum


class PaymentMethod(str, Enum):
    cash = "cash"
    credit_card = "credit_card"
    debit_card = "debit_card"
    e_wallet = "e_wallet"
    qris = "qris"
    bank_transfer = "bank_transfer"


class PaymentStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    success = "success"
    failed = "failed"
    refunded = "refunded"


class PaymentBase(BaseModel):
    order_id: UUID
    payment_method: PaymentMethod
    payment_gateway: Optional[str] = Field(None, max_length=100)
    amount: Decimal = Field(..., ge=0, decimal_places=2)


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    status: Optional[PaymentStatus] = None
    transaction_id: Optional[str] = Field(None, max_length=255)
    payment_url: Optional[str] = None
    paid_at: Optional[datetime] = None
    expired_at: Optional[datetime] = None
    gateway_response: Optional[Dict[str, Any]] = None


class PaymentInDB(PaymentBase):
    id: UUID
    transaction_id: Optional[str] = None
    status: PaymentStatus
    payment_url: Optional[str] = None
    paid_at: Optional[datetime] = None
    expired_at: Optional[datetime] = None
    gateway_response: Optional[Dict[str, Any]] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Payment(PaymentInDB):
    pass


class PaymentDetail(Payment):
    order_number: Optional[str] = None


class PaymentCallback(BaseModel):
    transaction_id: str
    status: str
    amount: Decimal
    signature: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None