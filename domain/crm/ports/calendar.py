from typing import Protocol
from domain.crm.entities.clientCalendar import ClientCalendar

class CmrCalendarPort(Protocol):
    
    async def getCalendar(self)->list | None:
        ...
        
    async def setCalendar(self, calendar) ->dict | None:
        ...