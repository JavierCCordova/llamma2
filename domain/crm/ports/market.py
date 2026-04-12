from typing import Protocol
from domain.ai import ports


class CmrMarketPort(Protocol):
    async def setMarketSave(self, market)->str | None:
        ...