from fastapi import FastAPI
from api.routes import router
from api.routers.ocr    import routerTesseract

app =   FastAPI()
app.include_router(router=router)
app.include_router(router=routerTesseract)