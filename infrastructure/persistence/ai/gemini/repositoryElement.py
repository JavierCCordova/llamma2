from domain.ai.ports import AIProviderProtocol
from infrastructure.persistence.ai.gemini.connection import GeminiConnexion
from infrastructure.persistence.mongodb.geminiRepository import GeminiRepository

class GeminiRepositoryElement(AIProviderProtocol):
    
    def __init__(self, geminiRepository:GeminiRepository, gemini : GeminiConnexion):
        self.geminiRepository   =   geminiRepository
        self.gemini             =   gemini
    async def generate(self, prompt): 
        return await self.gemini.generateResponse(prompt)
    
    async def getDataFile(self, file:bytes, *args)-> dict:
        prompt      =   await self.geminiRepository.getPrompt('general')
        response    =   await self.gemini.getExtractDocument(file,prompt,'application/pdf',*args)        
        return response
        