from core.config import settings
from bson import ObjectId

class MongoMarketRepository():
    
    def __init__(self, session):
        self.session    =   session
        self.db         =   self.session[ settings.DB_NAME]
        
    async def getData(self, idUser): 
        collection  =   self.db['aviciiSaveMarket']
        pipeline = [
            {
                "$match": {
                    "usuario_id": ObjectId(idUser)
                }
            },
            {
                "$unwind": "$items"
            },
            {
                "$project": {
                    "_id": 0,
                    "producto": {
                        "$toLower": "$items.producto"
                    },
                    "precio": "$items.precio_unitario",
                    "fecha": {
                            "$dateToString": {
                                "format": "%Y-%m-%d %H:%M:%S",
                                "date": "$fecha_captura"
                            }
                        }
                }
            },
            {
                "$sort": {
                    "producto": 1,
                    "fecha": 1
                }
            }
        ]
        cursor  =   collection.aggregate(pipeline)
        result  =   await cursor.to_list(length=None)
        return result
