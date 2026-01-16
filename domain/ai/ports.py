from typing import Protocol

class AIProviderProtocol(Protocol):
    async def generate(self, prompt: str) -> str: ... 