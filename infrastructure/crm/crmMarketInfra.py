from domain.crm.ports.market import CmrMarketPort
from infrastructure.persistence.mongodb.cmrMarketRepository import MongoCrmMarketRepository 

from domain.market.ports import MarketProviderPort
from infrastructure.persistence.mongodb.marketRepository import MongoMarketRepository

class MarketInfra(CmrMarketPort):
    
    def __init__(self, MongoCrmMarketRepository):
        self.mongoCrmMarketRepository   =   MongoCrmMarketRepository
    
    async def setMarketSave(self,market):
        return await self.mongoCrmMarketRepository.setMarketSave(market)
    
    
class MarketInfraProcess(MarketProviderPort):
    
    def __init__(self, MongoMarketRepository):
        self.mongoMarketRepository  =   MongoMarketRepository
        
    async def getData(self, idUser):
        return await self.mongoMarketRepository.getData(idUser) 