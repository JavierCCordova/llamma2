from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Item:
    producto: str
    cantidad: float
    unidad: str
    precio_unitario: float
    subtotal: float

@dataclass
class Totales:
    conteo_final: int
    monto_total_validado: float

@dataclass
class Mercado:
    usuario_id: str
    fecha_captura: datetime
    items: List[Item]
    totales: Totales