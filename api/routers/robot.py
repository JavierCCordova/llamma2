from fastapi import APIRouter, UploadFile, File, Form, Depends
from fastapi.responses  import JSONResponse
from api.dependencies import getCurrentUser, getDni, getIaResponse, getIaResponseMercado
from infrastructure.workers.tasks.ocrTask import process_ocr
from celery.result import AsyncResult
from infrastructure.workers.celeryApp import celery_app
from infrastructure.workers.tasks.ocrTask import test_task
import json

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


@routerRobot.post("/robot/ocrGemini")
async def getResponseIa(
    feature :   list[str] = Form(...),
    file    :   UploadFile | None = File(None),
    name    =   Depends(getCurrentUser),
    useCase =   Depends(getIaResponse)
):
    fileBytes           =   await file.read()
    response            =   {}
    response['status']  =   200  
    response['data']    =   await useCase.getDataFile(fileBytes, *feature)
    return JSONResponse(status_code=200, content=response)

@routerRobot.post("/robot/ocrMercado")
async def getResponseIaMercado(
    file    :   UploadFile | None = File(None),
    name    =   Depends(getCurrentUser),
    useCase =   Depends(getIaResponseMercado)
):
    fileBytes           =   await file.read()   
    response            =   {}
    response['status']  =   200  
    response['data']    =   await useCase.getDataImgMercado(fileBytes)
    return JSONResponse(status_code=200, content=response)
    
@routerRobot.post("/robot/ocrGeminiCelery")
async def getResponseIaCelery(
    feature :   list[str] = Form(...),
    file    :   UploadFile | None = File(None),
    name    =   Depends(getCurrentUser) 
):
    fileBytes   = await file.read()
    task        = process_ocr.delay(fileBytes, feature)
    return {
        "status": "processing",
        "task_id": task.id,
        "result_url": f"/robot/result/{task.id}"
    }

@routerRobot.get("/robot/result/{task_id}")
async def get_result(task_id: str):

    result = AsyncResult(task_id, app=celery_app)

    if result.ready():
        return {
            "status": "completed",
            "data": result.result
        }

    return {"status": "processing"}

@routerRobot.get("/testCelery")
async def testCelery():

    task = celery_app.send_task("tasks.test_task", args=[4,6])

    return {"task_id": task.id}