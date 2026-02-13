from domain.crm.ports.calendar import CmrCalendarPort
from infrastructure.persistence.mongodb.cmrRecordRepository import MongoCmrRecordRepository
from domain.crm.entities.clientCalendar import ClientCalendar

class CmrCalendarInfra(CmrCalendarPort):
    
    def __init__(self, mongoCmrRecordRepository:MongoCmrRecordRepository):
        self.mongoCmrRecordRepository   =mongoCmrRecordRepository
        
    async def getCalendar(self):
        return await self.mongoCmrRecordRepository.getCalendar()
        
    async def setCalendar(self, calendar: ClientCalendar):
        return await self.mongoCmrRecordRepository.setCalendar(calendar)