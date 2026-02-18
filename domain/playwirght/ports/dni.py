from typing import Protocol

class DniPort(Protocol):
    
    async def getNameWeb(self, dni: str) -> str | None:
        ...