from backend.app.audit.database import SessionLocal
from backend.app.audit.models import AuditLog


class AuditLogger:

    def log(
        self,
        prompt: str,
        model: str,
        status: str,
        decision: str,
        details: str = ""
    ):

        db = SessionLocal()

        try:

            record = AuditLog(
                user_prompt=prompt,
                model=model,
                status=status,
                decision=decision,
                details=details
            )

            db.add(record)
            db.commit()

        finally:
            db.close()
