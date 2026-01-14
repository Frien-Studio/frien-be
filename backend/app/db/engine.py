# app/db/engine.py
from sqlalchemy import create_engine
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,   # drops dead connections
    future=True           # SQLAlchemy 2.0 style
)
