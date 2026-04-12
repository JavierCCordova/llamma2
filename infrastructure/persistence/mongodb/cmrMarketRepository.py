from core.config import settings
from domain.ai.entity import Mercado

class MongoCrmMarketRepository():
    
    def __init__(self, session):
        self.session    =   session
        self.db         =   self.session[ settings.DB_NAME ]
        
    async def setMarketSave(self,market)-> str:
        collection  =   self.db['aviciiSaveMarket']
        res         =   await collection.insert_one(market)
        if res.inserted_id:
            return 1
        else:
            return 0