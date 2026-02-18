from fastapi import APIRouter, UploadFile, Depends
from fastapi.responses  import JSONResponse
from api.dependencies import getCurrentUser, getDni

routerRobot = APIRouter(prefix='/Robot', tags=['ROBOT'])

@routerRobot.post("/robot/dni")
async def getDataPage(
    dni     :   str,
    name    =   Depends(getCurrentUser),
    usecase =   Depends(getDni)
):
    response            =   {}
    response['status']  =   200
    data                =   await usecase.getNameWeb(dni)
    response['data']    =   data    
    return JSONResponse(status_code= 200, content=response)