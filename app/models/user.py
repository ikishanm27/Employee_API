from app.db import Base
from sqlalchemy import Column,Integer,String


class User(Base):
    __tablename__="Users"

    id=Column(Integer, primary_key=True, index=True)
    email=Column(String, unique= True, nullable=False)
    password=Column(String, nullable=False)
    role= Column(String, default="user")