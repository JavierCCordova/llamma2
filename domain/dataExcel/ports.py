from typing import Protocol
from domain.dataExcel.entities import ExcelFile

class ExcelRepositoryPort(Protocol):
    
    async def loadDataExcel(self, excel: ExcelFile)-> str: ...