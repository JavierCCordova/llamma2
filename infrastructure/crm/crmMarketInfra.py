from domain.crm.ports.market import CmrMarketPort
from infrastructure.persistence.mongodb.cmrMarketRepository import MongoCrmMarketRepository 

class MarketInfra(CmrMarketPort):
    
    def __init__(self, MongoCrmMarketRepository):
        self.mongoCrmMarketRepository   =   MongoCrmMarketRepository
    
    async def setMarketSave(self,market):
        return await self.mongoCrmMarketRepository.setMarketSave(market)