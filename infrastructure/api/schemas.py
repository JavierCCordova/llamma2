# infrastructure/api/schemas.py
from pydantic import BaseModel
from typing import List
from datetime import datetime

class ItemSchema(BaseModel):
    producto: str
    cantidad: float
    unidad: str
    precio_unitario: float
    subtotal: float

class TotalesSchema(BaseModel):
    conteo_final: int
    total_validado: float
    total_original_ocr: float

class MercadoInputSchema(BaseModel):
    usuario_id: str
    fecha_captura: datetime
    items: List[ItemSchema]
    totales: TotalesSchema