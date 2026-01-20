from domain.dataExcel.entities import ExcelFile
from infrastructure.excel.excelDataExcel import ExcelDataExcel

class DataExcelProcessing:
    
    def __init__(self, dataExcel: ExcelDataExcel):
        self.dataExcel  =   dataExcel
        
    async def loadExcelData(self, excel: ExcelFile):
        return await self.dataExcel.loadDataExcel(excel)