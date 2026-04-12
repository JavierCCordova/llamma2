from domain.crm.ports.record import CrmRecordPort 
from domain.crm.entities.clientId import ClientId
   
class CmrHistorytUseCase:
    
    def __init__(self, crmRecordPort  :   CrmRecordPort ) :
        self.crmRecordPort  =   crmRecordPort
        
    async def getCrmRecord(self, client: ClientId):   
        return await self.crmRecordPort.getCrmRecord(client)