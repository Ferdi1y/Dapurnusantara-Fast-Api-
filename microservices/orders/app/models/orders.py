from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Numeric, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
import enum
from app.db.base import Base


class OrderType(str, enum.Enum):
    dine_in = "dine_in"
    takeaway = "takeaway"
    delivery = "delivery"


class OrderStatus(str, enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    preparing = "preparing"
    ready = "ready"
    completed = "completed"
    cancelled = "cancelled"


class Orders(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), index=True)
    order_number = Column(String(50), unique=True, nullable=False)
    order_type = Column(Enum(OrderType), nullable=False)
    table_number = Column(String(20))
    delivery_address = Column(Text)
    subtotal = Column(Numeric(10, 2), nullable=False)
    tax = Column(Numeric(10, 2), default=0)
    discount = Column(Numeric(10, 2), default=0)
    delivery_fee = Column(Numeric(10, 2), default=0)
    total_amount = Column(Numeric(10, 2), nullable=False)
    status = Column(Enum(OrderStatus), nullable=False, default=OrderStatus.pending, index=True)
    notes = Column(Text)
    created_at = Column(DateTime(timezone=False), server_default=func.current_timestamp(), index=True)
    updated_at = Column(DateTime(timezone=False), server_default=func.current_timestamp(), onupdate=func.current_timestamp())

    # Relationships
    user = relationship("Users", back_populates="orders")
    order_items = relationship("OrderItems", back_populates="order", cascade="all, delete-orphan")
    payments = relationship("Payments", back_populates="order", cascade="all, delete-orphan")
    order_coupons = relationship("OrderCoupons", back_populates="order", cascade="all, delete-orphan")