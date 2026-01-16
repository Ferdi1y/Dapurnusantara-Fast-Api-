from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
from app.db.base import Base


class PaymentLogs(Base):
    __tablename__ = "payment_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    payment_id = Column(UUID(as_uuid=True), ForeignKey("payments.id", ondelete="CASCADE"))
    event_type = Column(String(100), nullable=False)
    event_data = Column(JSONB, nullable=False)
    ip_address = Column(String(50))
    created_at = Column(DateTime(timezone=False), server_default=func.current_timestamp())

    # Relationships
    payment = relationship("Payments", back_populates="payment_logs")