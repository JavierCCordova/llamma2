from domain.crm.ports.client import CmrClientPort 
from domain.crm.entities.clientId import ClientId

class CmrclienteUseCase:
    
    def __init__(self,
                 cmrClientPort  :   CmrClientPort 
                 ):
        self.cmrClientPort  =   cmrClientPort
        
    async def getCmrClient(self):
        return await self.cmrClientPort.getCmrClient()
    
    async def getCrmRecord(self, client: ClientId): 
        return await self.cmrClientPort.getCrmRecord(client)