from domain.market.ports import MarketProviderPort

class MarketUseCaseProcess:
    
    def __init__(self, marketProviderPort:MarketProviderPort):
        self.marketProviderPort   =   marketProviderPort
        
    async def getData(self,idUser):
        return await self.marketProviderPort.getData(idUser)
    