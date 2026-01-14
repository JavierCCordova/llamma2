from jose import jwt,JWTError
from datetime import datetime, timedelta, timezone
from  core.config import Settings

class TokenService:
    
    def __init__(self,settings: Settings):
        self.settings   =   settings
        
        
    def createAccessToken(self, data: dict):
        payload         =   data.copy()
        payload['exp']  =   datetime.now(timezone.utc) + timedelta(minutes=self.settings.ACCESS_TOKEN_EXPIRE_MINUTES)   
        return jwt.encode(payload, self.settings.SECRET_KEY, algorithm= "HS256")
        
    def verifyToken(self,token: str)-> str | None:
        try:
            payload     =   jwt.decode(
                token,
                self.settings.SECRET_KEY,
                algorithms=["HS256"]
            )
            return  payload.get("sub")            
        except JWTError:
            return None