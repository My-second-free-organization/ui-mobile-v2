from fastapi import FastAPI, UploadFile, File
from .processor import DocumentProcessor

app = FastAPI(title="FlowForge Document Processor", version="2.4.0")
processor = DocumentProcessor()

@app.post("/api/v1/documents/extract")
async def extract(file: UploadFile = File(...)): return await processor.extract(file)

@app.post("/api/v1/documents/classify")
async def classify(file: UploadFile = File(...)): return await processor.classify(file)

@app.get("/health")
def health(): return {"status": "healthy"}
