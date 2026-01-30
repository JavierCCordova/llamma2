from fastapi import APIRouter, UploadFile, Depends
from fastapi.responses import JSONResponse
from api.dependencies import getCurrentUser, getCmrCliente, getCrmRecord
from domain.crm.entities.clientId import ClientId

routerCmr   =   APIRouter(prefix= "/crm", tags= ['CRM'])

@routerCmr.get("/getclient")
async def getClientCMR(
    name    =   Depends(getCurrentUser),
    usecase =   Depends(getCmrCliente)
):  
    text    =   await usecase.getCmrClient()
    salida  =   {
        "status_code": 200,
        "message": "Datos recuperados con éxito",
        "client": text
    }
    return JSONResponse(content=salida, status_code=salida['status_code'])
    
@routerCmr.get("/getRecord")
async def getRecordCMR(
    idRecord:   int,
    name    =   Depends(getCurrentUser),
    usecase =   Depends(getCrmRecord),
):
    idRecordClient  =   ClientId(idRecord) 
    jsonRecord  =   await usecase.getCrmRecord(idRecordClient)
    salida  =   {
            "status_code": 200,
            "message": "Datos recuperados con éxito",
            "Data": jsonRecord
    }
    
    return JSONResponse(content=salida, status_code=salida['status_code'])
