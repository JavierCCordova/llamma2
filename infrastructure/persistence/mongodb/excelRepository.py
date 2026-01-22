from core.config import settings

class MongoExcelRepository():
    
    def __init__(self, session):
        self.session    =   session
        self.db         =   self.session[ settings.DB_NAME ]
        
    async def setDataExcel(self, info : dict)-> str | None:
        collection      =   self.db['aviciiDataPay']
        payCollection   =   await collection.insert_one(info)
        return 'Guardado' if payCollection.inserted_id  else None