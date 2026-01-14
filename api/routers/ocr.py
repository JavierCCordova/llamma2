from fastapi import APIRouter, UploadFile, Depends
from api.dependencies import getTesseractUseCase, getCurrentUser
from domain.tesseract.entities import PdfFile

routerTesseract    =    APIRouter(prefix="/ocr", tags=['OCR'])

@routerTesseract.post("/pdf")
async def extractText(
    file : UploadFile,
    name : str =    Depends(getCurrentUser),
    usecase = Depends(getTesseractUseCase)
):
    pdf     =   PdfFile(await file.read(), file.filename)
    text    =   await usecase.execute(pdf)
    return {'texto': text , 'usuario': name}