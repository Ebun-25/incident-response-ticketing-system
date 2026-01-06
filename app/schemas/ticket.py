from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TicketCreate(BaseModel):
    title: str
    description: str

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    category: Optional[str]
    priority: Optional[str]
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
