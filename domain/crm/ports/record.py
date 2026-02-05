from typing import Protocol
from domain.crm.entities.clientId import ClientId
from domain.crm.entities.clientRecord   import ClientRecord

class CrmRecordPort(Protocol):
    
    async def getCrmRecord(self, client: ClientId)-> dict | None:
        ...
        
    async def insertCrmRecord(self, record:ClientRecord) -> dict | None:
        ...
        
    async def deleteCrmRecord(self, id :str) -> dict | None:
        ...
        
    async def updateCrmRecord(self, record: ClientRecord, id :str)-> bool | None:
        ...