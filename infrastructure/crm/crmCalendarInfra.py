from domain.crm.ports.calendar import CmrCalendarPort
from infrastructure.persistence.mongodb.cmrRecordRepository import MongoCmrRecordRepository

class CmrCalendarInfra(CmrCalendarPort):
    
    def __init__(self, mongoCmrRecordRepository:MongoCmrRecordRepository):
        self.mongoCmrRecordRepository   =mongoCmrRecordRepository
        
    async def getCalendar(self):
        return await self.mongoCmrRecordRepository.getCalendar()
        