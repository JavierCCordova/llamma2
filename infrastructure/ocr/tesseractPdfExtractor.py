from domain.tesseract.ports import pdfTextExtractorPort
from domain.tesseract.entities import PdfFile

class TesseractpdfExtractor(pdfTextExtractorPort):
     
    async def extractText(self, pdf: PdfFile)->str:
        #codigo de tesseract para aplicar
        texto   =   "holamundoPrueba"
        return texto