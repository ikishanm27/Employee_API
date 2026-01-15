from pydantic import BaseModel, EmailStr



class Userregister(BaseModel):
    email: EmailStr
    password: str

class Userlogin(BaseModel):
    email: EmailStr
    password : str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        # orm_mode = True
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
