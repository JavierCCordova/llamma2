from domain.crm.ports.record import CrmRecordPort


class CmrDeleteUseCase:
    
    def __init__(self, crmRecordPort:CrmRecordPort):
         self.crmRecordPort =   crmRecordPort

    async def deleteCrmRecord(self,id: str):
        return await self.crmRecordPort.deleteCrmRecord(id)