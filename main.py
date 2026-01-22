from fastapi import FastAPI
from api.routes import router
from api.routers.ocr    import routerTesseract
from api.routers.dataExcel import routerDataExcel
## Exception
from api.exceptionHandlers import domainErrorHandler
from domain.common.exceptions import DomainError

app =   FastAPI()
app.include_router(router = router)
app.include_router(router = routerTesseract)
app.include_router(router = routerDataExcel)

app.add_exception_handler(DomainError,domainErrorHandler)