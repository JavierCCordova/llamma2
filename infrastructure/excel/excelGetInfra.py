from infrastructure.persistence.mongodb.excelRepository  import MongoExcelRepository
from domain.dataExcel.ports.sumaryPort import SummaryPort

class ExcelGetInfra(SummaryPort):
    def __init__(self,mongoExcelRepository: MongoExcelRepository ):
        self.mongoExcelRepository   =   mongoExcelRepository
    
    async def gePaySummary(self,  idSummary: str)-> dict  :
        return await self.mongoExcelRepository.getMongoPaySummary(idSummary)