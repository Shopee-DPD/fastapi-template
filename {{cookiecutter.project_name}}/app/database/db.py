from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.settings.config import DatabaseSettings

db_settings = DatabaseSettings()

engine = create_engine(
    URL.create(**db_settings.model_dump()),
    pool_pre_ping=True,
    pool_recycle=300,
)


class Base(DeclarativeBase):
    pass


Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
