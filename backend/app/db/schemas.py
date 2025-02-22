from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


# Base schema for common user attributes
class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


# Schema for employee-specific data
class EmployeeBase(BaseModel):
    hire_date: date
    salary: float
    manager_id: Optional[int] = None


# Schema for manager-specific data
class ManagerBase(BaseModel):
    department: str


# Schema for creating an employee (includes user data and employee data)
class CreateEmployee(BaseModel):
    user: UserBase  # User data
    employee: EmployeeBase  # Employee-specific data


# Schema for updating an employee
class UpdateEmployee(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    hire_date: Optional[date] = None
    salary: Optional[float] = None
    manager_id: Optional[int] = None


# Schema for creating a manager (includes user data and manager data)
class CreateManager(BaseModel):
    user: UserBase  # User data
    manager: ManagerBase  # Manager-specific data


# Schema for updating a manager
class UpdateManager(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[str] = None


# Schema for updating an employee's manager
class UpdateEmployeesManager(BaseModel):
    manager_id: int = None
