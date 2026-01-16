from core.config import settings
import google.generativeai as genai

class GeminiConnexion:
    
    _client = None
    
    def getClient(self):        
        if self._client is None:
            self._client    =   genai.client(api_key = settings.KEY_GEMINI_LLAMA)
        return self._client
        