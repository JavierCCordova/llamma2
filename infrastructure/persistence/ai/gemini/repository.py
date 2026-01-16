from domain.ai.ports import AIProviderProtocol
from infrastructure.persistence.ai.gemini.connection import GeminiConnexion

class GeminiAiRepository(AIProviderProtocol):
    
    async def generate(self, fileUpdate: bytes ,prompt: str, model: str)-> str:
        client      =   GeminiConnexion.getClient()
        filePath    =   client.files.upload(
            file    =   fileUpdate
        )
        response    =   client.models.generate_content(
            model   =   model,
            contents=   [filePath, prompt]
        )
        
        if not response or not response.text:
            raise Exception("Ai empty response")
        
        return response