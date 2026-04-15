from domain.crm.ports.market import CmrMarketPort

class MarketUseCase:
    
    def __init__(self, cmrMarketPort: CmrMarketPort):
        self.cmrMarketPort  =   cmrMarketPort
        
    async def setMarketSave(self, market)->str:
        return await self.cmrMarketPort.setMarketSave(market)
    