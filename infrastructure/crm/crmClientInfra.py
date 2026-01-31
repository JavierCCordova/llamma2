from domain.crm.ports.client import CmrClientPort
from infrastructure.persistence.mongodb.cmrClientRepository import MongoCmrClientRepository

class ClientInfra(CmrClientPort):
    
    def __init__( self,
                  mongoCmrRepository:MongoCmrClientRepository):
        self.mongoCmrRepository =   mongoCmrRepository
    
    async def getCmrClient(self): 
        return await self.mongoCmrRepository.getCmrClient()