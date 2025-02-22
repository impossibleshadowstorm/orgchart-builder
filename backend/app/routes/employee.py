from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import User, Employee, Manager
from app.db.schemas import CreateEmployee, UpdateEmployee, UpdateEmployeesManager
from app.core.exceptions import NotFoundException, BadRequestException
from datetime import date
from typing import List

router = APIRouter()


# Get all employees
@router.get("/", response_model=List[dict], status_code=status.HTTP_200_OK)
def get_all_employees(db: Session = Depends(get_db)):
    # Fetch all employees
    employees = db.query(Employee).all()
    if not employees:
        return []

    # Construct the response
    response = []
    for employee in employees:
        # Fetch the associated user
        user = db.query(User).filter(User.user_id == employee.user_id).first()

        # Fetch the manager details if manager_id exists
        manager = None
        if employee.manager_id:
            manager = (
                db.query(Manager)
                .filter(Manager.manager_id == employee.manager_id)
                .first()
            )

        # Append employee details to the response
        response.append(
            {
                "employee_id": employee.employee_id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "hire_date": employee.hire_date,
                "salary": employee.salary,
                "manager": (
                    {
                        "manager_id": manager.manager_id,
                        "first_name": manager.user.first_name,
                        "last_name": manager.user.last_name,
                        "department": manager.department,
                    }
                    if manager
                    else None
                ),
            }
        )

    return response


# Get an employee by ID
@router.get("/{employee_id}", status_code=status.HTTP_200_OK)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    # Fetch the employee
    employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if not employee:
        raise NotFoundException(resource="employee", id=employee_id)

    # Fetch the associated user
    user = db.query(User).filter(User.user_id == employee.user_id).first()

    # Fetch the manager details if manager_id exists
    manager = None
    if employee.manager_id:
        manager = (
            db.query(Manager).filter(Manager.manager_id == employee.manager_id).first()
        )

    # Construct the response
    response = {
        "employee_id": employee.employee_id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "hire_date": employee.hire_date,
        "salary": employee.salary,
        "manager": (
            {
                "manager_id": manager.manager_id,
                "first_name": manager.user.first_name,
                "last_name": manager.user.last_name,
                "department": manager.department,
            }
            if manager
            else None
        ),
    }

    return response


# Create an employee
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_employee(employee_data: CreateEmployee, db: Session = Depends(get_db)):
    # Check if the user already exists
    existing_user = (
        db.query(User).filter(User.email == employee_data.user.email).first()
    )
    if existing_user:
        raise BadRequestException(detail="User with this email already exists")

    # ✅ Validate manager_id if provided
    if employee_data.employee.manager_id:
        manager_exists = (
            db.query(Manager)
            .filter(Manager.manager_id == employee_data.employee.manager_id)
            .first()
        )
        if not manager_exists:
            raise BadRequestException(
                detail="Invalid manager_id. Manager does not exist."
            )

    # Create the user
    new_user = User(
        first_name=employee_data.user.first_name,
        last_name=employee_data.user.last_name,
        email=employee_data.user.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Create the employee
    new_employee = Employee(
        user_id=new_user.user_id,
        hire_date=employee_data.employee.hire_date,
        salary=employee_data.employee.salary,
        manager_id=employee_data.employee.manager_id,
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return {
        "message": "Employee created successfully",
        "employee_id": new_employee.employee_id,
    }


# Update an employee
@router.patch("/{employee_id}", status_code=status.HTTP_200_OK)
def update_employee(
    employee_id: int, employee_data: UpdateEmployee, db: Session = Depends(get_db)
):
    # Fetch the employee
    employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if not employee:
        raise NotFoundException(resource="employee", id=employee_id)

    # ✅ Validate manager_id if provided
    if employee_data.manager_id:
        manager_exists = (
            db.query(Manager)
            .filter(Manager.manager_id == employee_data.manager_id)
            .first()
        )
        if not manager_exists:
            raise BadRequestException(
                detail="Invalid manager_id. Manager does not exist."
            )

    # Fetch the associated user
    user = db.query(User).filter(User.user_id == employee.user_id).first()

    # Update user data if provided
    if employee_data.first_name:
        user.first_name = employee_data.first_name
    if employee_data.last_name:
        user.last_name = employee_data.last_name
    if employee_data.email:
        user.email = employee_data.email

    # Update employee data if provided
    if employee_data.hire_date:
        employee.hire_date = employee_data.hire_date
    if employee_data.salary:
        employee.salary = employee_data.salary
    if employee_data.manager_id:
        employee.manager_id = employee_data.manager_id

    db.commit()
    db.refresh(employee)

    return {"message": "Employee updated successfully", "employee": employee_data}


# Update an employee's manager
@router.patch("/{employee_id}/manager", status_code=status.HTTP_200_OK)
def update_employee_manager(
    employee_id: int,
    manager_data: UpdateEmployeesManager,
    db: Session = Depends(get_db),
):
    if not manager_data.manager_id:
        raise BadRequestException(detail="manager_id required.")

    # Fetch the employee
    employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if not employee:
        raise NotFoundException(resource="employee", id=employee_id)

    # ✅ Validate manager_id if provided
    if manager_data.manager_id:
        manager_exists = (
            db.query(Manager)
            .filter(Manager.manager_id == manager_data.manager_id)
            .first()
        )
        if not manager_exists:
            raise BadRequestException(
                detail="Invalid manager_id. Manager does not exist."
            )

    # Update the manager_id
    employee.manager_id = manager_data.manager_id
    db.commit()
    db.refresh(employee)

    return {"message": "Employee's manager updated successfully", "employee": employee}
