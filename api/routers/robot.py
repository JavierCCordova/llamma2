from fastapi import APIRouter, UploadFile, Depends
from fastapi.responses  import JSONResponse
from api.dependencies import getCurrentUser, getDni, getIaResponse

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

@routerRobot.post("/robot/resultGemini")
async def getResponseIa(
    question    :   str,
    name    =   Depends(getCurrentUser),
    useCase =   Depends(getIaResponse)
):
    response            =   {}
    response['status']  =   200
    response['data']    =   await useCase.generate(question)
    return JSONResponse(status_code=200, content=response)