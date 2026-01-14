from typing import Protocol, Optional
from domain.user.entities import UserEntity

class UserRepositoryPort(Protocol):
    async def getByUserName(self, userName: str) ->Optional[UserEntity]:
        ...
        #return userEntity(id=1, userName="Holamundo",hashPassword="holamundo2")
    #userRepository