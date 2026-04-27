from typing import Protocol

class MarketProviderPort(Protocol):
    
    async def getData(self, idUser: str)-> list: 
        ...