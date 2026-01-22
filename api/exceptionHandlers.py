from fastapi import Request
from fastapi.responses import JSONResponse
from domain.common.exceptions import DomainError

async def domainErrorHandler(request: Request, exc: DomainError):
    return JSONResponse(
        status_code= 400,
        content= {
             "statusCode": 400,
             "message": str(exc)
        }
    )