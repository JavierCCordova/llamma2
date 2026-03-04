from core.config import settings
import google.generativeai as genai
import json
import re

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
    
    async def _formatPrompt(self, *args):
        features    =   "\n".join(f"- {x}" for x in args)
        dictExtract =   {x: "" for x in args}
        jsonExample =   json.dumps(dictExtract, ensure_ascii=False)
        prompt      = (
                f"{features}\n\n"
                f"Documentos:\n"
                f"Salida esperada (ejemplo de formato):\n"
                f"{jsonExample}"
            ).strip() 
        return prompt

    async def _clearJsonResponse(self, text: str):        
        clearText   =   re.sub(r"```json|```", "", text).strip()
        try:
            jsonReps    =   json.loads(clearText) 
        except json.JSONDecodeError:
            jsonReps   =   clearText.encode().decode("unicode_escape")
            jsonReps   =   json.loads(jsonReps)
        finally:
            return jsonReps

    async def getExtractDocument(self, file: bytes ,prompt:str, mimeType: str, *args)->dict:
        promptFo    =   await self._formatPrompt(*args)
        promptFi    =   f"{prompt} \n {promptFo}"
        filePart    =   {
            "mime_type": mimeType,
            "data": file
        }
        response    =   await self._model.generate_content_async(
            contents=[
                promptFi,
                filePart
            ]
        )
        
        return await self._clearJsonResponse(response.text)
        
         