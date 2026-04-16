from domain.ai.entity import Mercado, Item, Totales

def toDomainMarket(schema):
    return Mercado(
        usuario_id= schema.usuario_id,
        fecha_captura= schema.fecha_captura,
        items=[
            Item(**item.dict()) for item in schema.items
        ],
        totales=Totales(**schema.totales.dict())
    )
    
def mercadoToDict(domain_obj):
    return {
        "usuario_id": domain_obj.usuario_id,
        "fecha_captura": domain_obj.fecha_captura, 
        "items": [
            {
                "producto": item.producto,
                "cantidad": item.cantidad,
                "unidad": item.unidad,
                "precio_unitario": item.precio_unitario,
                "subtotal": item.subtotal,
            }
            for item in domain_obj.items
        ],
        "totales": {
            "conteo_final": domain_obj.totales.conteo_final,
            "total_validado": domain_obj.totales.total_validado,
            "total_original_ocr": domain_obj.totales.total_original_ocr,
        }
    }