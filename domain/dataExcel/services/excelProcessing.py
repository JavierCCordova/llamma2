from domain.dataExcel.entities import ExcelFile
from domain.common.exceptions import InvalidFormatError

class ExcelValidationService:
    
    def validateExcel(self, excel: ExcelFile):
        if not excel.filename.endswith('.xlsx'):
            raise InvalidFormatError("Formato no válido")
    
    def extractMetaData(self, excel: ExcelFile) -> dict:
        return {
            "filename": excel.filename,
            "size": len(excel.content)
        }