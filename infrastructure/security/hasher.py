from passlib.context import CryptContext

passHash    =   CryptContext( schemes=   ["argon2"] ,deprecated="auto")

class PasswordHasher:
    
    def hash(self, passw:str)->str:
        return passHash.hash(passw)
    
    def verify(self, plain:str, hashed: str)-> bool:
        return passHash.verify(plain, hashed)