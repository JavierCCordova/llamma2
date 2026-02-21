from core.config import settings
import google.generativeai as genai

class GeminiConnexion:
    
    _client = None
    
    def __init__(self, modelName: str = 'gemini-2.5-flash'):
        genai.configure(api_key = settings.KEY_GEMINI_LLAMA)
        self._model =   genai.GenerativeModel(modelName)
    
    async def generateResponse(self, prompt):        
        try:
            response    =   await self._model.generate_content_async(prompt)
            if not response.text:
                return 'No tenemos respuesta de la IA'
            
            return  response.text
        except:
            return 'Problemas con la solución'