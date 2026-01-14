
from domain.user.ports import UserRepositoryPort
from domain.user.entities   import UserEntity
from core.config import settings

class MongoRepository(UserRepositoryPort):
    
    def __init__(self, session):
        self.session    =   session
        self.db         =   self.session[settings.DB_NAME]        
        self.collection =   self.db['aviciiUser']
        
    async def getByUserName(self, username: str)->UserEntity | None:        
        userCollection  =   await self.collection.find_one({'username':username})
        if not userCollection:
            return None
         
        return UserEntity(
            id          =   str(userCollection['_id']),
            userName    =   userCollection['username'] ,
            hashPassword=   userCollection['password'] 
        )
        