from domain.dataExcel.entities  import  ExcelFile
from domain.dataExcel.ports     import  ExcelRepositoryPort

class ExcelDataExcel(ExcelRepositoryPort):
    
    async def loadDataExcel(self, excel: ExcelFile)-> str:
        return 'HolamundoExcel'