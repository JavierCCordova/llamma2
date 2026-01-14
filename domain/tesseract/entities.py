class PdfFile:
    
    def __init__(self, content: bytes, filename: str):
        self.content    =   content
        self.filename   =   filename