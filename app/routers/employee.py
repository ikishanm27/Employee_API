from fastapi import APIRouter,Depends
from app.services.employee import *
from app.schemas.employee import CreateEmployee, UpdateEmployee
from sqlalchemy.orm import Session
from app.db import get_db
from typing import Optional
from app.security.checkrole import require_admin

router=APIRouter(prefix="/api")

@router.post("/employees")
def create_employee(emp: CreateEmployee, db:Session=Depends(get_db)):
    return create_service(emp,db)

@router.get("/employees")
def all_employees(page:int=1, limit:int=5,department: Optional[str] = None,
    role: Optional[str] = None, db:Session=Depends(get_db), admin=Depends(require_admin)):

    return all_service(page, limit, department, role, db)

@router.get("/employee")
def single_employee(id:int, db:Session=Depends(get_db), admin=Depends(require_admin)):
    return single_service(id,db)

@router.put("/employee")
def update_employee(id :int,update_employee: UpdateEmployee, db:Session=Depends(get_db), admin=Depends(require_admin)):
    return update_service(id,update_employee , db)

@router.delete("/employee")
def delete_employee(id:int, db:Session=Depends(get_db),  admin=Depends(require_admin)):
    return delete_service(id,db)

