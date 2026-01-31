from datetime import datetime
from pydantic import BaseModel

class ClientRecord(BaseModel):
    
    idClient    :   int
    dateRecord  :   datetime
    dateAgent   :   datetime
    description :   str
    typeAccion  :   str
    responseAction  :   str
    