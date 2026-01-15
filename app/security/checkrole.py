from fastapi import Depends,HTTPException,status
from app.security.oauth2 import get_current_user

def require_admin(user=Depends(get_current_user)):
    if user["role"]!="admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="only admin are allowed")
    return user