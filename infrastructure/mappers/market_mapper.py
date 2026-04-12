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