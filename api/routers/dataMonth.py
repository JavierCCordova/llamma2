from fastapi import APIRouter, UploadFile, Depends
from domain.dataExcel.entities import ExcelFile
from api.dependencies import getCurrentUser, getExcelUseCase

routerdataMonth =   APIRouter(prefix="/data", tags=['DATA'])

@routerdataMonth.post("/excel")
async def importExcel(
    file        :   UploadFile,
    depJwt      :   str =   Depends(getCurrentUser),  #jwt    
    usecase     =   Depends(getExcelUseCase)
):
    excelClass  =   ExcelFile(await file.read(), file.filename) 
    response    =   await usecase.loadExcelData(excelClass)
    print(response)
    return  {'procesado': 'prueba', 'datos':depJwt}