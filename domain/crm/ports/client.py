from typing import Protocol 
from domain.crm.entities.clientId import ClientId

class CmrClientPort(Protocol):
    
    async def getCmrClient(self)-> dict | None:
        ...
    
    async def getCrmRecord(self, client: ClientId)-> dict | None:
        ...