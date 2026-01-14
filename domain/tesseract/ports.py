from typing import Protocol
from domain.tesseract.entities import PdfFile

class pdfTextExtractorPort(Protocol):
    async def extractText(self,pdf : PdfFile)-> str: ...