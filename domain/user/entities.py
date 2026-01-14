from pydantic import BaseModel

class UserEntity(BaseModel):
    
    id:             str
    userName:       str
    hashPassword:   str