from domain.crm.ports.record import CrmRecordPort
from infrastructure.persistence.mongodb.cmrRecordRepository import MongoCmrRecordRepository

class RecordInfra(CrmRecordPort):
    
    def __init__(self, mongoCmrRecordRepository:MongoCmrRecordRepository):
        self.mongoCmrRecordRepository   =   mongoCmrRecordRepository
        
    async def insertCrmRecord(self, record):
        return await self.mongoCmrRecordRepository.insertCrmRecord(record)
    
    async def getCrmRecord(self, client): 
        return await self.mongoCmrRecordRepository.getCmrRecord(client)
    
    
    async def deleteCrmRecord(self, id):
        return await self.mongoCmrRecordRepository.deleteCrmRecord(id)