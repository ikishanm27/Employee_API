from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta


pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")


def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain:str, hashed:str):
    return pwd_context.verify(plain, hashed)


Secret_key="2ceinwar"
Algorithm="HS256"


def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp":expire})

    return jwt.encode(to_encode, Secret_key,algorithm=Algorithm)    


