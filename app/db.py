from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./employees.db"

engine=create_engine(connect_args={"check_same_thread": False}, db_url)
SessionLocal=sessionmaker((autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


