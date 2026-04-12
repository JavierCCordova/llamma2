from core.config import settings
from domain.crm.entities.clientRecord import ClientRecord
from domain.crm.entities.clientId import ClientId
from domain.crm.entities.clientCalendar import ClientCalendar
from datetime import datetime
from bson import ObjectId 

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
    
    async def deleteCrmRecord(self,id: str) -> dict:
        Idbyson     =   ObjectId(id)
        collection  =   self.db['aviciiCmrRecord']
        delAcc      =   await collection.delete_one({'_id':Idbyson})
        
        response    =   {
            "status" :  "sucess" if delAcc.deleted_count > 0 else "No registros" 
        }
        
        return response
    
    def toMongoDict(self, record: ClientRecord):
        return record.model_dump()
    
    async def updateCrmRecord(self, record: ClientRecord, id: str)->bool:
        try:
            collection  =   self.db['aviciiCmrRecord']
            dataMongo   =   self.toMongoDict(record) 
            result      =   await collection.update_one(
                { "_id": ObjectId(id) },
                 {"$set": dataMongo }
            )
            return result.modified_count > 0 
        except Exception as e: 
            return False
        
    async def getCalendar(self)-> list:
        try:
            response    =   []
            collection  =   self.db['aviciiCmrCalender']
            dataCal     =   collection.find()
            calendar    =   await dataCal.to_list(length=None)
            if calendar:
                for x in calendar:
                    rawDate =   x.get('date')
                    if rawDate:
                        formatDate = rawDate.strftime("%Y-%m-%d")
                    
                    respo   =   {
                         "date":        formatDate, 
                         "descripcion": x.get('descripcion',''), 
                         "cliente":     x.get('cliente','')
                    }
                    response.append(respo)
            return response
        except Exception as e:
            return False
    
    async def setCalendar(self,calendar: ClientCalendar) -> dict:
        
        collection  =   self.db['aviciiCmrCalender']
        calendar    =   calendar.model_dump()
        result      =   await collection.insert_one(calendar)
        nuevoId     =   str(result.inserted_id)
         
        return {
            "status" :  200 if nuevoId else 500,
            "message":  "success" if nuevoId else "Error",
        }