from fastapi import APIRouter, UploadFile, File, Form, Depends
from fastapi.responses  import JSONResponse
from api.dependencies import getCurrentUser
from api.dependencies import (getMarketProcess)

routerMarket = APIRouter(prefix = '/Market', tags=['Market'])

@routerMarket.get('/market/data')
async def getDataMarket(
    idUser  =   str,
    name    =   Depends(getCurrentUser),
    usecase =   Depends(getMarketProcess)
):  
    response    =   {}
    response['status']  =   200
    response['data']    =  await usecase.getData(idUser)
    return JSONResponse(status_code= 200,content=response)