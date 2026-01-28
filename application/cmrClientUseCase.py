from domain.crm.ports.client import CmrClientPort 

class CmrclienteUseCase:
    
    def __init__(self,
                 cmrClientPort  :   CmrClientPort 
                 ):
        self.cmrClientPort  =   cmrClientPort
        
    async def getCmrClient(self):
        return await self.cmrClientPort.getCmrClient()