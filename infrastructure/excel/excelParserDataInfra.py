import pandas as pd
from datetime import datetime

class PandasParser:
    
    def getReportPayExcel(self, dataExcel: bytes)->dict:
        df          =   pd.read_excel(dataExcel)
        
        ##      ==========================================================  ##
        
        df['Mes']   =   pd.to_datetime(df['Mes'])
        df['Mes']   =   df['Mes'].dt.to_period("M")

        faltantes   =   []
        
        for (cliente, concepto), grupo in df.groupby(["Cliente", "Concepto"]):
            mesMin = grupo["Mes"].min()
            mesMax = grupo["Mes"].max()
            allMonth  = pd.period_range(mesMin, mesMax, freq="M")
            mesPresente  = set(grupo["Mes"])

            for mes in allMonth:
                faltantes.append({
                    "Cliente": cliente,
                    "Concepto": concepto,
                    "meses": mes,
                    "Faltante": "Exite" if mes in mesPresente else "No Esta"
                })

        dfFaltantes = pd.DataFrame(faltantes).sort_values(
            by = ["Cliente", "Concepto", "meses"],
            ascending= [False, False, True]
        )
        
        dfFaltantes['meses']  =   dfFaltantes['meses'].astype(str)
        
        ##      ==========================================================  ##
        
        faltanteInfo  = []
        df['Fecha de\nEmisión']  =  pd.to_datetime(df['Fecha de\nEmisión'])
        df['EmisionPeriodo']     =  df['Fecha de\nEmisión'].dt.to_period('M')

        for (cliente, concepto), grupo in df.groupby(["Cliente", "Concepto"]):

            min_emision = grupo["EmisionPeriodo"].min()
            max_emision = grupo["EmisionPeriodo"].max()

            all_months = pd.period_range(min_emision, max_emision, freq="M")

            mesPresenteClien = set(grupo["EmisionPeriodo"])
            mesFaltanteClien = sorted(set(all_months) - mesPresenteClien)

            for mes in mesFaltanteClien:
                faltanteInfo.append({
                    "Cliente": cliente,
                    "Concepto": concepto,
                    "meses": mes,
                    "Faltante": "Falta"
                })

            for mes in mesPresenteClien:
                faltanteInfo.append({
                    "Cliente": cliente,
                    "Concepto": concepto,
                    "meses": mes,
                    "Faltante": "Llego"
                })         
        
        dfFaltantesEmision = (
                                pd.DataFrame(faltanteInfo)
                                .sort_values(
                                    by=["Cliente", "Concepto", "meses"],
                                    ascending=[True, True, False]
                                ).reset_index(drop=True)
                            )       
        
        
        dfFaltantesEmision['meses']  =   dfFaltantesEmision['meses'].astype(str)
        
        ##      ==========================================================  ##
                
        return {
                    'fechaCreacion': datetime.now(),
                    'faltante': dfFaltantes.to_dict(orient="records"), 
                    'emision':  dfFaltantesEmision.to_dict(orient="records")
                }