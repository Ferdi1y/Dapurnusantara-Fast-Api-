from sqlalchemy import Column, DateTime, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
from app.db.base import Base


class OrderCoupons(Base):
    __tablename__ = "order_coupons"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id", ondelete="CASCADE"))
    coupon_id = Column(UUID(as_uuid=True), ForeignKey("coupons.id", ondelete="SET NULL"))
    discount_amount = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime(timezone=False), server_default=func.current_timestamp())

    # Relationships
    order = relationship("Orders", back_populates="order_coupons")
    coupon = relationship("Coupons", back_populates="order_coupons")