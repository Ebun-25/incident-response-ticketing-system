from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.incident import Incident
from app.models.ticket import Ticket
from app.schemas.incident import IncidentResponse

router = APIRouter(prefix="/incidents", tags=["Incidents"])

@router.post("/{ticket_id}", response_model=IncidentResponse)
def create_incident(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        return {"error": "Ticket not found"}

    incident = Incident(
        ticket_id=ticket.id,
        severity=ticket.priority,
        description=ticket.description
    )

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return incident
