from fastapi import FastAPI

from backend.app.api.chat import router as chat_router
from backend.app.api.audit import router as audit_router

from backend.app.audit.database import engine, Base


# Create tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="LLM Security Platform",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(chat_router)
app.include_router(audit_router)
