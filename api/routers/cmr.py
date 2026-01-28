from fastapi import APIRouter, UploadFile, Depends
from fastapi.responses import JSONResponse
from api.dependencies import getCurrentUser, getCmrCliente

routerCmr   =   APIRouter(prefix= "/crm", tags= ['CRM'])

@routerCmr.get("/getclient")
async def getClientCMR(
    name    =   Depends(getCurrentUser),
    usecase =   Depends(getCmrCliente)
):  
    text    =   await usecase.getCmrClient()
    salida  =   {
        "client": text,
        "status_code": 200,
        "message": "Datos recuperados con éxito"
    }
    return JSONResponse(content=salida, status_code=salida['status_code'])
    