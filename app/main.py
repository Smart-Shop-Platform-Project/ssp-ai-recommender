from fastapi import FastAPI
import logging
import sys
from .api.recommender_routes import router as recommender_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='{"time":"%(asctime)s", "level":"%(levelname)s", "message":"%(message)s"}',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("ssp-ai-recommender")

app = FastAPI(title="SSP AI Recommender")

app.include_router(recommender_router, prefix="/api/v1")

@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "SSP AI Recommender is running"}
