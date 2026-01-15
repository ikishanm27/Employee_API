from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class CreateEmployee(BaseModel):
    name:str
    email:EmailStr
    department: Optional[str]=None
    role: Optional[str]=None


class ResponseEmployee(BaseModel):
    id: int
    name:str
    email:EmailStr
    department:Optional[str]
    role:Optional[str]
    date_joined:datetime

    class Config:
        from_attributes=True

class UpdateEmployee(BaseModel):
    name: Optional[str]=None
    email:Optional[EmailStr]=None
    department: Optional[str]=None
    role:Optional[str]=None
        
