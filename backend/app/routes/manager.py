from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import User, Manager
from app.db.schemas import CreateManager, UpdateManager
from app.core.exceptions import NotFoundException, BadRequestException
from datetime import date
from typing import List

router = APIRouter()


# Get all managers
@router.get("/", response_model=List[dict], status_code=status.HTTP_200_OK)
def get_all_employees(db: Session = Depends(get_db)):
    # Fetch all managers
    managers = db.query(Manager).all()
    if not managers:
        return []

    # Construct the response
    response = []
    for manager in managers:
        # Append managers details to the response
        response.append(
            {
                "manager_id": manager.manager_id,
                "first_name": manager.user.first_name,
                "last_name": manager.user.last_name,
                "department": manager.department,
                "email": manager.user.email,
            }
        )

    return response


# Create a manager
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_manager(manager_data: CreateManager, db: Session = Depends(get_db)):
    # Check if the user already exists
    existing_user = db.query(User).filter(User.email == manager_data.user.email).first()
    if existing_user:
        raise BadRequestException(detail="User with this email already exists")

    # Create the user
    new_user = User(
        first_name=manager_data.user.first_name,
        last_name=manager_data.user.last_name,
        email=manager_data.user.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Create the manager
    new_manager = Manager(
        user_id=new_user.user_id,
        department=manager_data.manager.department,
    )
    db.add(new_manager)
    db.commit()
    db.refresh(new_manager)

    return {
        "message": "Manager created successfully",
        "manager_id": new_manager.manager_id,
    }


# Update a manager
@router.patch("/{manager_id}", status_code=status.HTTP_200_OK)
def update_manager(
    manager_id: int, manager_data: UpdateManager, db: Session = Depends(get_db)
):
    # Fetch the manager
    manager = db.query(Manager).filter(Manager.manager_id == manager_id).first()
    if not manager:
        raise NotFoundException(resource="manager", id=manager_id)

    # Fetch the associated user
    user = db.query(User).filter(User.user_id == manager.user_id).first()

    # Update user data if provided
    if manager_data.first_name:
        user.first_name = manager_data.first_name
    if manager_data.last_name:
        user.last_name = manager_data.last_name
    if manager_data.email:
        user.email = manager_data.email

    # Update manager data if provided
    if manager_data.department:
        manager.department = manager_data.department

    db.commit()
    db.refresh(manager)

    return {"message": "Manager updated successfully"}
