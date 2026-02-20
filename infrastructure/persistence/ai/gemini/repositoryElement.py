from domain.ai.ports import AIProviderProtocol
from infrastructure.persistence.ai.gemini.connection import GeminiConnexion

class GeminiRepositoryElement(AIProviderProtocol):
    
    async def generate(self, prompt):
        gemini  =   GeminiConnexion()
        return await gemini.generateResponse(prompt)