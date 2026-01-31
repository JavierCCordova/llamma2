from domain.crm.entities.clientRecord import ClientRecord 
from domain.crm.ports.record import CrmRecordPort

class CmrInsertUseCase:
    
    def __init__(self, crmRecordPort : CrmRecordPort):
        self.crmRecordPort = crmRecordPort
        
    async def insertCrmRecord(self, clientRecord: ClientRecord):
        return await self.crmRecordPort.insertCrmRecord(clientRecord)