from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime

from backend.app.audit.database import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    timestamp = Column(DateTime, default=datetime.utcnow)

    user_prompt = Column(Text)

    model = Column(String)

    status = Column(String)

    decision = Column(String)

    details = Column(Text)
