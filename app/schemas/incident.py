from pydantic import BaseModel
from datetime import datetime

class IncidentResponse(BaseModel):
    id: int
    ticket_id: int
    severity: str
    status: str
    description: str
    created_at: datetime

    class Config:
        from_attributes = True
