from fastapi import FastAPI

from app.database import engine, Base
from app.models import ticket, incident
from app.api.tickets import router as ticket_router
from app.api.incidents import router as incident_router

app = FastAPI(
    title="AI-Powered Incident Response & Ticket Triage System",
    version="0.1.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(ticket_router)
app.include_router(incident_router)

# Health check
@app.get("/")
def health_check():
    return {"status": "running"}
