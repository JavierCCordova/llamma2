from domain.crm.ports.client import CmrClientPort
from infrastructure.persistence.mongodb.cmrRepository import MongoCmrRepository

class ProcessingInfra(CmrClientPort):
    
    def __init__( self,
                  mongoCmrRepository:MongoCmrRepository):
        self.mongoCmrRepository =   mongoCmrRepository
    
    async def getCmrClient(self): 
        return await self.mongoCmrRepository.getCmrClient()
    
    async def getCrmRecord(self, client: int): 
        return await self.mongoCmrRepository.getCmrRecord(client)