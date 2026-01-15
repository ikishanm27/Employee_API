from app.schemas.employee import CreateEmployee, UpdateEmployee
from sqlalchemy.orm import Session
from app.models.employee import Employee
from fastapi import HTTPException, status





def create_service(emp : CreateEmployee, db:Session):
    db_employee=db.query(Employee).filter(Employee.email==emp.email).first()
    if db_employee:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="user already registered")
    
    new_emp=Employee(**emp.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp




def all_service(page, limit, department, role, db:Session):
    offset=(page-1)*limit

    query = db.query(Employee)

    # Apply filters only if provided
    if department:
        query = query.filter(Employee.department == department)

    if role:
        query = query.filter(Employee.role == role)

    total = query.count()

    employees = query.offset(offset).limit(limit).all()

    return {
        "page":page,
        "limit":limit,
        "total":total,
        "data":employees
    }

def single_service(id:int, db: Session):
    employee=db.query(Employee).filter(Employee.id==id).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="employee not found")
    return employee




def update_service(id,  update_employee:UpdateEmployee, db: Session):
    db_employee=db.query(Employee).filter(Employee.id==id).first()
    
    if not db_employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="employee not found")
    
    for key,value in update_employee.dict(exclude_unset=True).items():
        setattr(db_employee,key,value)

    db.commit()
    db.refresh(db_employee)
    return db_employee




def delete_service(id:int, db :Session):
    db_employee=db.query(Employee).filter(Employee.id==id).first()
    if not db_employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="employee not found")
    
    db.delete(db_employee)
    db.commit()
    return {"message":"Employee deleted successfully"}
