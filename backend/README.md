# FASTAPI OrgChart

## Overview

**FASTAPI OrgChart** is a RESTful API built with FastAPI to manage an organizational hierarchy of employees and managers. It provides endpoints to create, update, and retrieve employee and manager details while ensuring data integrity and validation using Pydantic and SQLAlchemy.

## Features

- **Employee Management**: CRUD operations for employees.
- **Manager Management**: CRUD operations for managers.
- **Role-Based Association**: Employees can be associated with managers.
- **Validation & Error Handling**: Uses Pydantic for request validation and custom exception handling.
- **Database Support**: Uses PostgreSQL with SQLAlchemy ORM.
- **Docker Support**: Easily deployable with Docker.

## Tech Stack

- **FastAPI** - Web framework for APIs
- **SQLAlchemy** - ORM for database management
- **Alembic** - Database migrations
- **PostgreSQL** - Database
- **Docker** - Containerization

## File Structure

```
app
├── core
│   ├── config
│   ├── exceptions
│   ├── logger
├── db
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
├── routes
│   ├── __init__.py
│   ├── employee.py
│   ├── manager.py
├── main.py
.env
.gitignore
DockerFile
requirements.txt
```

## Installation

### Prerequisites

- Python 3.10+
- PostgreSQL
- Docker (optional for containerization)

### Clone the Repository

```sh
git clone https://github.com/impossibleshadowstorm/orgchart-builder.git
cd fastapi-orgchart
```

### Configure Environment Variables

Create a `.env` file in the backend and frontend folder with the .env.example content in both folders respectively.

### Run with Docker

---

#### Go to Project folder

```sh
cd fastapi-orgchart
```

#### Run docker commands

```sh
docker build
docker compose up
```

### Run without Docker

---

#### Install Dependencies

Create a virtual environment and install dependencies:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

#### Run Database Migrations

```sh
alembic upgrade head
```

#### Run the Application

```sh
uvicorn app.main:app --reload
```

## API Endpoints

### Employee Endpoints

| Method | Endpoint                  | Description                  |
| ------ | ------------------------- | ---------------------------- |
| GET    | `/employees/`             | Get all employees            |
| GET    | `/employees/{id}`         | Get employee by ID           |
| POST   | `/employees/`             | Create a new employee        |
| PATCH  | `/employees/{id}`         | Update an employee           |
| PATCH  | `/employees/{id}/manager` | Update an employee's manager |

### Manager Endpoints

| Method | Endpoint         | Description          |
| ------ | ---------------- | -------------------- |
| GET    | `/managers/`     | Get all managers     |
| POST   | `/managers/`     | Create a new manager |
| PATCH  | `/managers/{id}` | Update a manager     |

## Error Handling

The API returns structured error messages with appropriate HTTP status codes:

```json
{
  "detail": "User with this email already exists"
}
```
