from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Numeric, Enum
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
import enum
from app.db.base import Base


class PaymentMethod(str, enum.Enum):
    cash = "cash"
    credit_card = "credit_card"
    debit_card = "debit_card"
    e_wallet = "e_wallet"
    qris = "qris"
    bank_transfer = "bank_transfer"


class PaymentStatus(str, enum.Enum):
    pending = "pending"
    processing = "processing"
    success = "success"
    failed = "failed"
    refunded = "refunded"


class Payments(Base):
    __tablename__ = "payments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id", ondelete="CASCADE"), index=True)
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    payment_gateway = Column(String(100))
    transaction_id = Column(String(255), unique=True, index=True)
    amount = Column(Numeric(10, 2), nullable=False)
    status = Column(Enum(PaymentStatus), nullable=False, default=PaymentStatus.pending, index=True)
    payment_url = Column(Text)
    paid_at = Column(DateTime(timezone=False))
    expired_at = Column(DateTime(timezone=False))
    gateway_response = Column(JSONB)
    created_at = Column(DateTime(timezone=False), server_default=func.current_timestamp())
    updated_at = Column(DateTime(timezone=False), server_default=func.current_timestamp(), onupdate=func.current_timestamp())

    # Relationships
    order = relationship("Orders", back_populates="payments")
    payment_logs = relationship("PaymentLogs", back_populates="payment", cascade="all, delete-orphan")