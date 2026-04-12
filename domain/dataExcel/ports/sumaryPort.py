from typing import Protocol

class SummaryPort(Protocol):
    
    async def gePaySummary(self, idSummary)-> dict | None:
        ...
    