import boto3
from ..core.config import settings
import logging
import json

logger = logging.getLogger("ssp-ai-recommender")

class RecommenderService:
    def __init__(self):
        self.sagemaker_runtime = boto3.client('sagemaker-runtime', region_name=settings.AWS_REGION)

    async def get_recommendations(self, user_id: str, num_recommendations: int):
        if not settings.SAGEMAKER_ENDPOINT_NAME or "placeholder" in settings.SAGEMAKER_ENDPOINT_NAME:
            logger.error("SageMaker endpoint is not configured")
            raise Exception("SageMaker endpoint not configured")
            
        try:
            logger.info(f"Invoking SageMaker endpoint {settings.SAGEMAKER_ENDPOINT_NAME} for user {user_id}")
            payload = json.dumps({"user_id": user_id, "num_recommendations": num_recommendations})
            
            response = self.sagemaker_runtime.invoke_endpoint(
                EndpointName=settings.SAGEMAKER_ENDPOINT_NAME,
                ContentType='application/json',
                Body=payload
            )
            
            result = json.loads(response['Body'].read().decode())
            return result
        except Exception as e:
            logger.error(f"Failed to get recommendations for user {user_id}: {e}")
            raise
