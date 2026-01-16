from sqlalchemy import Column, String, Boolean, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
import enum
from app.db.base import Base


class UserRole(str, enum.Enum):
    customer = "customer"
    staff = "staff"
    admin = "admin"


class Users(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(20))
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=False), server_default=func.current_timestamp())
    updated_at = Column(DateTime(timezone=False), server_default=func.current_timestamp(), onupdate=func.current_timestamp())

    # Relationships
    orders = relationship("Orders", back_populates="user")