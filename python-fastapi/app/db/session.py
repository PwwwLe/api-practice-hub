from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from app.db.base import Base

def get_db() -> Generator[Session, None, None]:
    """ 生成器，用于获取数据库会话 """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()