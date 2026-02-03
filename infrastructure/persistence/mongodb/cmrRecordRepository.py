from core.config import settings
from domain.crm.entities.clientRecord import ClientRecord
from domain.crm.entities.clientId import ClientId
from datetime import datetime

class MongoCmrRecordRepository():
    
    def __init__(self, session):
        self.session    =   session
        self.db         =   self.session[ settings.DB_NAME ]
        
    async def getCmrRecord(self, client: ClientId)->dict: 
        collection  =   self.db['aviciiCmrRecord']  
        clientColl  =   collection.find({'idClient': client.idClient})
        recordsCall =   await clientColl.to_list(length=None)
        response = []
        for r in recordsCall: 
            
            date_rec = r.get('dateRecord', '')
            date_age = r.get('dateAgent', '')
 
            if isinstance(date_rec, datetime):
                date_rec = date_rec.isoformat()
            if isinstance(date_age, datetime):
                date_age = date_age.isoformat()

            response.append({
                "id"            : str(r.get('_id')),
                "dateRecord"    : date_rec,
                "dateAgent"     : date_age,
                "description"   : r.get('description', ''),
                "typeAccion"    : r.get('typeAccion', ''),
                "responseAction": r.get('responseAction', '')
            })
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