from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.app.audit.database import SessionLocal
from backend.app.audit.models import AuditLog


router = APIRouter(prefix="/audit")


@router.get("/logs")
def get_logs(limit: int = 100):

    db: Session = SessionLocal()

    try:

        logs = (
            db.query(AuditLog)
            .order_by(AuditLog.timestamp.desc())
            .limit(limit)
            .all()
        )

        return [
            {
                "id": l.id,
                "timestamp": l.timestamp,
                "prompt": l.user_prompt,
                "model": l.model,
                "status": l.status,
                "decision": l.decision,
                "details": l.details
            }
            for l in logs
        ]

    finally:
        db.close()
