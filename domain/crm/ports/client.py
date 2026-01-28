from typing import Protocol


class CmrClientPort(Protocol):
    
    async def getCmrClient(self)-> dict | None:
        ...