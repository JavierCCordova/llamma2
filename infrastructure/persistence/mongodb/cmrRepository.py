from core.config import settings
from domain.crm.entities.clientId import ClientId

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
    
    async def getCmrRecord(self, client: ClientId)->dict:
        #response    =   {}
        collection  =   self.db['aviciiCmrRecord']  
        clientColl  =   collection.find({'id_client': client.idClient})
        recordsCall =   await clientColl.to_list(length=None)
        response    =   [
            {
                "date_record": r.get('date_record', ''),
                "date_agent": r.get('date_agent', ''),
                "description": r.get('description', ''),
                "type_accion": r.get('type_accion', ''),
                "response_action": r.get('response_action', '')
            }
            for r in recordsCall
        ]
        
        return response