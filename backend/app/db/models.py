from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship
from app.db.database import Base


# Base table for common attributes
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    # Relationships
    employee = relationship("Employee", back_populates="user", uselist=False)
    manager = relationship("Manager", back_populates="user", uselist=False)


# Employee table
class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    hire_date = Column(Date, nullable=False)
    salary = Column(Numeric(10, 2), nullable=False)
    manager_id = Column(Integer, ForeignKey("managers.manager_id"), nullable=False)

    # Relationships
    user = relationship("User", back_populates="employee")
    manager = relationship("Manager", back_populates="employees")  # Link to Manager table

# Manager table
class Manager(Base):
    __tablename__ = "managers"

    manager_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    department = Column(String(100), nullable=False)

    # Relationships
    user = relationship("User", back_populates="manager")
    employees = relationship("Employee", back_populates="manager")