from fastapi import APIRouter, HTTPException
from ..services.recommender_service import RecommenderService

router = APIRouter()
recommender_service = RecommenderService()

@router.post("/recommendations", tags=["Recommendations"])
async def get_recommendations(user_id: str, num_recommendations: int = 5):
    try:
        return await recommender_service.get_recommendations(user_id, num_recommendations)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
