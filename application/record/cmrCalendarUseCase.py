from domain.crm.entities.clientCalendar import ClientCalendar
from domain.crm.ports.calendar import CmrCalendarPort

class CmrCalendarUseCase:
    
    def __init__(self, cmrCalendarPort: CmrCalendarPort):
        self.cmrCalendarPort    =   cmrCalendarPort
        
    async def getCalendar(self):
        return await self.cmrCalendarPort.getCalendar()