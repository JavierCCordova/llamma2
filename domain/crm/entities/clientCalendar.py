from pydantic import BaseModel
from datetime import datetime

class ClientCalendar(BaseModel):
    date:           datetime
    descripcion:    str
    cliente:        str