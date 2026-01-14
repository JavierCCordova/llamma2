from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings

class MongoClientManager:
    _cliente    : AsyncIOMotorClient    =   None
    
    @classmethod
    def getCliente(cls)->AsyncIOMotorClient:
        if cls._cliente is None:
            cls._cliente    =   AsyncIOMotorClient(settings.MONGO_URL)
        return cls._cliente
    
    @classmethod
    def close_db(cls):
        if cls._cliente:
            cls._cliente.close()
    