from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schemas.user import Userlogin, Userregister, UserOut, Token
from app.services.user import userlogin, userregister, showusers
from app.db import get_db
from app.security.oauth2 import get_current_user
from app.models.user import User
from app.security.checkrole import require_admin


user=APIRouter(prefix="/user")

@user.post("/register", response_model=UserOut)
def register(user : Userregister,db: Session=Depends(get_db)):
    return userregister(user,db)

@user.post("/login", response_model=Token)
def login(user : Userlogin, db: Session=Depends(get_db)):
    return userlogin(user,db)

@user.get("/all")
def get_current_user_profile(db :Session=Depends(get_db), page :int=1 , limit:int=5, admin=Depends(require_admin)):
    return showusers(page,  limit, db)