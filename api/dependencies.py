from fastapi import Depends
from application.authUseCase import LoginUseCase
from infrastructure.security.hasher import PasswordHasher
from infrastructure.security.tokenService import TokenService
from core.config import getSettings
from infrastructure.persistence.mongodb.connection import MongoClientManager
from infrastructure.persistence.mongodb.userRepository import MongoRepository
## tesseract
from application.tesseractUseCase import ExtractTextTesseract
from infrastructure.ocr.tesseractPdfExtractor import TesseractpdfExtractor
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