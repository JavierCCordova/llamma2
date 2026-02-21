from typing import Protocol

class AIProviderProtocol(Protocol):
    async def generate(self, prompt: str) -> str: ... 
    
    async def getDataFile(self, file: bytes, *args) -> dict:
        ...
    