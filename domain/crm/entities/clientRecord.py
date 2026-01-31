from datetime import date
from pydantic import BaseModel

class ClientRecord(BaseModel):
    
    idClient    :   int
    dateRecord  :   date
    dateAgent   :   date
    description :   str
    typeAccion  :   str
    responseAction  :   str
    