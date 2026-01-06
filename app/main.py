from fastapi import FastAPI
from app.database import engine, Base
from app.models import ticket
from app.api.tickets import router as ticket_router

app = FastAPI(
    title="AI-Powered Incident Response & Ticket Triage System",
    version="0.1.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(ticket_router)

@app.get("/")
def health_check():
    return {"status": "running"}
