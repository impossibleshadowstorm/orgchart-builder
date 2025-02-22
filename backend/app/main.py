from fastapi import FastAPI
from app.routes import employee, manager
from app.db.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Project", description="A Simple Org chart App.", version="1.0.0"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(employee.router, prefix="/api/employee", tags=["Employee"])
app.include_router(manager.router, prefix="/api/manager", tags=["Manager"])
