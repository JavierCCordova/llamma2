from fastapi import APIRouter, UploadFile, Depends
from domain.dataExcel.entities import ExcelFile
from api.dependencies import getCurrentUser, getExcelUseCase

routerDataExcel =   APIRouter(prefix="/data", tags=['DATA'])

@routerDataExcel.post("/excel/payments")
async def importExcelPay(
    file        :   UploadFile,
    depJwt      :   str =   Depends(getCurrentUser),  #jwt    
    usecase     =   Depends(getExcelUseCase)
):
    excelClass  =   ExcelFile(await file.read(), file.filename) 
    response    =   await usecase.loadExcelData(excelClass)
    print(response)
    return  {'procesado': 'prueba', 'datos':depJwt, "resultado": response}

@routerDataExcel.get("/excel/payments/summary")
async def obtainExcelPay(
    idFile  :   str,
    depJwt  :   str = Depends(getCurrentUser),
    
):  
    print(idFile)
    return {'Salida': 'Holamundo'}