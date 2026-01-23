from fastapi import Depends
from application.authUseCase import LoginUseCase
from infrastructure.security.hasher import PasswordHasher
from infrastructure.security.tokenService import TokenService
from core.config import getSettings
from infrastructure.persistence.mongodb.connection import MongoClientManager
from infrastructure.persistence.mongodb.userRepository import MongoRepository
## tesseract ##
from application.tesseractUseCase import ExtractTextTesseract
from infrastructure.ocr.tesseractPdfExtractor import TesseractpdfExtractor
##
##  Excel ##
from application.excelUseCase import DataExcelUseCase, GetSummaryUseCase
from infrastructure.excel.excelData import DataExcel
from infrastructure.excel.excelGetInfra import ExcelGetInfra
from infrastructure.excel.excelParserDataInfra import PandasParser
from infrastructure.persistence.mongodb.excelRepository import MongoExcelRepository
from domain.dataExcel.services.excelProcessing  import ExcelValidationService
##
## JWT  ##
from fastapi import HTTPException
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
## 
jwtBearToken    =   HTTPBearer()

async def getUserRepository():
    mongoClient  =   MongoClientManager.getCliente()
    return MongoRepository(mongoClient)

async def getLoginUseCase(settings = Depends(getSettings)):
    
    repo    =  await getUserRepository()
    
    return LoginUseCase(
        userRepo=       repo,
        hasher=         PasswordHasher(),
        tokenService=   TokenService(settings)
    )
    
async def getCurrentUser(
    credentials: HTTPAuthorizationCredentials   =   Depends(jwtBearToken),
    settings    =   Depends(getSettings)
):
    token          =    credentials.credentials
    tokenService   =   TokenService(settings)
    userId         =   tokenService.verifyToken(token)
    if not userId:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    return userId
    
async def getTesseractUseCase():
    return ExtractTextTesseract(TesseractpdfExtractor())

async def getExcelUseCase(): 
    
    mongoClient     =   MongoClientManager.getCliente()    ##trae session
    mongoRepository =   MongoExcelRepository(mongoClient)
    validation      =   ExcelValidationService()
    pandasParser    =   PandasParser()
    return DataExcelUseCase(DataExcel(mongoRepository,pandasParser),
                            validation)
    
async def getSummaryDepende():
    
    mongoclient     =   MongoClientManager.getCliente()
    MongoRepository =   MongoExcelRepository(mongoclient)
    validation      =   ExcelValidationService()
    return GetSummaryUseCase( ExcelGetInfra(MongoRepository), validation)
    