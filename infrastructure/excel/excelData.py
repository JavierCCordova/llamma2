from domain.dataExcel.entities  import  ExcelFile
from domain.dataExcel.ports     import  ExcelRepositoryPort
from infrastructure.persistence.mongodb.excelRepository  import MongoExcelRepository
from infrastructure.excel.excelParserDataInfra import PandasParser

class DataExcel(ExcelRepositoryPort):
    
    def __init__(
                    self,mongoExcelRepository: MongoExcelRepository,
                    pandasParser: PandasParser
                 ):
        self.mongoExcelRepository   =   mongoExcelRepository
        self.pandasParser           =   pandasParser
    
    async def loadDataExcel(self, excel: ExcelFile)-> dict:
        responseParser  =   self.pandasParser.getDataExcel(excel.content)
        return responseParser
        
        
    async def saveDataExcel(self, data: dict) -> str | None:
        return await self.mongoExcelRepository.setDataExcel(data)