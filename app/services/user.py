from app.schemas.user import Userregister, Userlogin
from sqlalchemy.orm import Session
from app.models.user import User
from fastapi import HTTPException
from app.security.security import hash_password, verify_password, create_access_token


def userregister(user: Userregister, db: Session):
    db_user=db.query(User).filter(User.email==user.email).first()
    if db_user:
        raise HTTPException(status_code=409, detail="User already exists")
    hashed_password=hash_password(user.password)
    new_user=User(email=user.email, password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def userlogin(user: Userlogin, db: Session): 
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token =create_access_token({"sub":user.email, "role":db_user.role})
    return {"access_token": token, "token_type": "bearer"}

def showusers(page: int, limit:int, db:Session,):
    offset=(page-1)*limit
    users=(db.query(User).offset(offset).limit(limit).all())
    total=db.query(User).count()

    return{
        "page":page,
        "limit":limit,
        "total":total,
        "data":users
    }