from domain.user.ports import UserRepositoryPort
from infrastructure.security.hasher import PasswordHasher
from infrastructure.security.tokenService import TokenService

class LoginUseCase:
    
    def __init__(self, 
                 userRepo: UserRepositoryPort, 
                 hasher:PasswordHasher, 
                 tokenService: TokenService):
        self.userRepo       =   userRepo    #Objeto de domain, que se declara en memoria.
        self.hasher         =   hasher  
        self.tokenService   =   tokenService
        
    async def execute(self, username: str, password: str):
        user    =   await self.userRepo.getByUserName(username) 
        if not user or not self.hasher.verify(password,user.hashPassword):
            raise Exception("Credenciales invalidas")
        
        return self.tokenService.createAccessToken({'sub': user.userName})