from sqlalchemy import Column, String, Text, Boolean, DateTime, Integer, Numeric, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
import enum
from app.db.base import Base


class DiscountType(str, enum.Enum):
    percentage = "percentage"
    fixed = "fixed"


class Coupons(Base):
    __tablename__ = "coupons"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    code = Column(String(50), unique=True, nullable=False, index=True)
    description = Column(Text)
    discount_type = Column(Enum(DiscountType), nullable=False)
    discount_value = Column(Numeric(10, 2), nullable=False)
    min_purchase = Column(Numeric(10, 2), default=0)
    max_discount = Column(Numeric(10, 2))
    usage_limit = Column(Integer)
    used_count = Column(Integer, default=0)
    valid_from = Column(DateTime(timezone=False))
    valid_until = Column(DateTime(timezone=False))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=False), server_default=func.current_timestamp())
    updated_at = Column(DateTime(timezone=False), server_default=func.current_timestamp(), onupdate=func.current_timestamp())

    # Relationships
    order_coupons = relationship("OrderCoupons", back_populates="coupon")