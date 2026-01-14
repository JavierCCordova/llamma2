
class ExtractTextTesseract:
    
    def __init__(self, extractor):
        self.extractor  =   extractor
        
    async def execute(self, pdf):
        return await self.extractor.extractText(pdf)
        