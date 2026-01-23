from core.config import settings
from bson import ObjectId

class MongoExcelRepository():
    
    def __init__(self, session):
        self.session    =   session
        self.db         =   self.session[ settings.DB_NAME ]
        
    async def setDataPayExcel(self, info : dict)-> str | None:
        
        collection      =   self.db['aviciiDataPay']
        payCollection   =   await collection.insert_one(info)
        return 'Guardado' if payCollection.inserted_id  else None
    
    async def getMongoPaySummary(self, idSummary: str)-> dict | None:
        
        collection      =   self.db['aviciiDataPay']
        summaryRespon   =   await collection.find_one({'_id': ObjectId(idSummary)})
        if summaryRespon:
            return summaryRespon.get('emision',{})