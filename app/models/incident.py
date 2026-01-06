from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"), nullable=False)

    severity = Column(String, nullable=False)
    status = Column(String, default="open")
    description = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
