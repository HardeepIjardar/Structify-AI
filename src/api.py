from fastapi import FastAPI
from src.models import NormalizeRequest
from src.pipeline import NormalizationPipeline

app = FastAPI()
pipeline = NormalizationPipeline()


@app.post("/normalize")
async def normalize(request: NormalizeRequest):
    return await pipeline.normalize(request)
