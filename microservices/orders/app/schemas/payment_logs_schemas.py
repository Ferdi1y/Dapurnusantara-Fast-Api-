from pydantic import BaseModel, Field, ConfigDict
from typing import Dict, Any, Optional
from datetime import datetime
from uuid import UUID


class PaymentLogBase(BaseModel):
    payment_id: UUID
    event_type: str = Field(..., max_length=100)
    event_data: Dict[str, Any]
    ip_address: Optional[str] = Field(None, max_length=50)


class PaymentLogCreate(PaymentLogBase):
    pass


class PaymentLogInDB(PaymentLogBase):
    id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PaymentLog(PaymentLogInDB):
    pass