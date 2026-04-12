from domain.dataExcel.entities import ExcelFile
from domain.common.exceptions import InvalidFormatError, InvalidSizeInput

class ExcelValidationService:
    
    def validateExcel(self, excel: ExcelFile):
        if not excel.filename.endswith('.xlsx'):
            raise InvalidFormatError("Formato no válido")
    
    def extractMetaData(self, excel: ExcelFile) -> dict:
        return {
            "filename": excel.filename,
            "size": len(excel.content)
        }
        
    def validateSideCharSummaryExcel(self, idSummary: str)->bool:
        if len(idSummary)< 10:
            raise InvalidSizeInput("El tamaño del campos es mejore de lo esperado")        