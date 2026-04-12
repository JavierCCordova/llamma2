from typing import Protocol 
from domain.crm.entities.clientId import ClientId
from domain.crm.entities.clientRecord   import ClientRecord

class CmrClientPort(Protocol):
    
    async def getCmrClient(self)-> dict | None:
        ...