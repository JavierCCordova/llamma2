from core.config import settings

class MongoCmrRepository():
    
    def __init__(self, session):
        self.session    =   session
        self.db         =   self.session[ settings.DB_NAME ]
        
    
    async def getCmrClient(self)->dict: 
        response    =   {}
        collection  =   self.db['aviciiCmrClient']
        clientColl  =   collection.find()
        clients     =   await clientColl.to_list(length=None)
        if clients:
            for client in clients:
                responseClient = {
                            #"Id":       client.get('id_client', ''),
                            "client":   client.get('client', ''),
                            "ruc":      client.get('ruc', ''),
                            "telefono": client.get('telefono', '')
                        }
                response[client.get('id_client', '')] =    responseClient
        return response