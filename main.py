from fastapi import FastAPI
from api.routes import router
from api.routers.ocr    import routerTesseract
from api.routers.dataMonth import routerdataMonth

app =   FastAPI()
app.include_router(router = router)
app.include_router(router = routerTesseract)
app.include_router(router = routerdataMonth)