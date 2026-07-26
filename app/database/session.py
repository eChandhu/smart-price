from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import get_settings

from typing import Generator
from sqlalchemy.orm import Session

settings = get_settings()

engine = create_engine(
    settings.database_url,
    echo=False,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

def get_db() -> Generator[Session, None, None]:
    """
    Create a database session for each request.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()