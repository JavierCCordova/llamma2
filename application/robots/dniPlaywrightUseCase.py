from domain.playwirght.ports.dni import DniPort

class DniUseCase:
    
    def __init__(self,   
                 dniPort: DniPort): 
        self.dniPort    =   dniPort
        
    async def getNameWeb(self, dni):
        return await self.dniPort.getNameWeb(dni)
        
    