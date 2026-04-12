from domain.dataExcel.entities import ExcelFile 
from domain.dataExcel.port import ExcelRepositoryPort 
from domain.dataExcel.ports.sumaryPort import SummaryPort 
from domain.dataExcel.services.excelProcessing import ExcelValidationService

class DataExcelUseCase:
    
    def __init__(self,  dataExcel: ExcelRepositoryPort,
                        validation: ExcelValidationService
                    ):
        self.dataExcel  =   dataExcel
        self.validation =   validation
        
    async def loadExcelData(self, excel: ExcelFile):
        self.validation.validateExcel(excel)
        data    =    await self.dataExcel.loadDataExcel(excel)
        return await self.dataExcel.saveDataExcel(data)
    

class GetSummaryUseCase:
    
    def __init__(self,  sumaryPort: SummaryPort,
                        validation: ExcelValidationService
                    ):
        self.sumaryPort  =   sumaryPort
        self.validation =   validation
        
    async def getSummaryUseCase(self, idSummary: str ) ->dict:
        self.validation.validateSideCharSummaryExcel(idSummary=idSummary)
        return await self.sumaryPort.gePaySummary(idSummary)