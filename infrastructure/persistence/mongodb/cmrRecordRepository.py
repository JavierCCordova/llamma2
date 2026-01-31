from core.config import settings
from domain.crm.entities.clientRecord import ClientRecord
from domain.crm.entities.clientId import ClientId

class MongoCmrRecordRepository():
    
    def __init__(self, session):
        self.session    =   session
        self.db         =   self.session[ settings.DB_NAME ]
        
    async def getCmrRecord(self, client: ClientId)->dict:
        print("getCmrRecord Repository", client.idClient)
        collection  =   self.db['aviciiCmrRecord']  
        clientColl  =   collection.find({'idClient': client.idClient})
        recordsCall =   await clientColl.to_list(length=None)
        response    =   [
            {
                "dateRecord"    : r.get('dateRecord', ''),
                "dateAgent"     : r.get('dateAgent', ''),
                "description"   : r.get('description', ''),
                "typeAccion"    : r.get('typeAccion', ''),
                "responseAction": r.get('responseAction', '')
            }
            for r in recordsCall
        ]
        
        return response
    
    async def insertCrmRecord(self, record : ClientRecord) -> dict:
        try:
            collection  =   self.db['aviciiCmrRecord']  
            collecInse  =   await collection.insert_one(record.model_dump())
            
            response    = {
                "status" : 'success'  if collecInse.acknowledged  else 'error',
                "id": str(collecInse.inserted_id)
            }
            return response
        except Exception as e:
            print(e)
            response    =   {
                "status" : "error",
                "message": "Error de BBDD"
            }
            return response