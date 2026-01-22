import pandas as pd

class PandasParser:
    
    def getDataExcel(self, dataExcel: bytes)->dict:
        df = pd.read_excel(dataExcel)
        return {
            'rows': len(df),
            "columns": list(df.columns)
        }
        