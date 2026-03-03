from fastapi import UploadFile
import io

class DocumentProcessor:
    async def extract(self, file: UploadFile) -> dict:
        content = await file.read()
        return {"filename": file.filename, "size": len(content), "extracted_fields": {}, "confidence": 0.95}

    async def classify(self, file: UploadFile) -> dict:
        content = await file.read()
        return {"filename": file.filename, "classification": "invoice", "confidence": 0.92}
