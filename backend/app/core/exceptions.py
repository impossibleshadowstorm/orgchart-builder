from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.core.logger import logger


def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTP Exception: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled Exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred."},
    )


# Custom Not Found Exception
class NotFoundException(HTTPException):
    def __init__(self, resource: str, id: int):
        detail = f"{resource.capitalize()} with ID {id} not found"
        super().__init__(status_code=404, detail=detail)


# Not Found Exception Handler
def not_found_exception_handler(request: Request, exc: NotFoundException):
    logger.error(f"Not Found Exception: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


# Custom Bad Request Exception
class BadRequestException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)


# Bad Request Exception Handler
def bad_request_exception_handler(request: Request, exc: BadRequestException):
    logger.error(f"Bad Request Exception: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )
