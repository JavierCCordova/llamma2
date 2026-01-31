from fastapi import FastAPI
from api.routes import router
from api.routers.ocr    import routerTesseract
from api.routers.dataExcel import routerDataExcel
from api.routers.crm import routerCmr
## Exception
from api.exceptionHandlers import domainErrorHandler
from domain.common.exceptions import DomainError

from fastapi.middleware.cors import CORSMiddleware

app =   FastAPI()
app.include_router(router = router)
app.include_router(router = routerTesseract)
app.include_router(router = routerDataExcel)
app.include_router(router = routerCmr)

app.add_exception_handler(DomainError,domainErrorHandler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
