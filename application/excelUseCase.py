from domain.dataExcel.entities import ExcelFile 
from domain.dataExcel.ports import ExcelRepositoryPort 
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