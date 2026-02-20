from domain.ai.ports import AIProviderProtocol

class GeminiUseCase:
    
    def __init__(self, aiprovider : AIProviderProtocol):
        self.Aiprovider =   aiprovider
        
    async def generate(self,prompt: str)-> str:
        return await self.Aiprovider.generate(prompt)