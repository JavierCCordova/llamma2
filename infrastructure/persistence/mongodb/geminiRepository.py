from core.config import settings

class GeminiRepository():
    
    def __init__(self, session):
        self.session    =   session
        self.db         =   self.session[ settings.DB_NAME ]
        
    async def getPrompt(self, type: str)-> str:
        collection  =   self.db['aviciiPrompt']
        res         =   await collection.find_one({'client':type})  
        response    =   res.get('prompt','') if res else ''
        return response
        