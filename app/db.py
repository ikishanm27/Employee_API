from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_url="postgresql://postgres:1234@localhost:5432/postgres"

engine=create_engine(db_url)
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


