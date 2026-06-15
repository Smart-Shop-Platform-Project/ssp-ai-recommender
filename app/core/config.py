from pydantic_settings import BaseSettings
import os
import boto3
import logging

logger = logging.getLogger("ssp-ai-recommender")

def get_ssm_parameter(name, region):
    try:
        ssm_client = boto3.client('ssm', region_name=region)
        parameter = ssm_client.get_parameter(Name=name, WithDecryption=True)
        return parameter['Parameter']['Value']
    except Exception as e:
        logger.critical(f"Error fetching parameter {name}: {e}")
        raise

class Settings(BaseSettings):
    AWS_REGION: str = os.environ.get("AWS_REGION", "us-east-1")
    SAGEMAKER_ENDPOINT_NAME_PARAM: str = os.environ.get("SAGEMAKER_ENDPOINT_NAME_PARAM", "/ssp/ai/recommender_endpoint_name")
    SAGEMAKER_ENDPOINT_NAME: str = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.SAGEMAKER_ENDPOINT_NAME = get_ssm_parameter(self.SAGEMAKER_ENDPOINT_NAME_PARAM, self.AWS_REGION)
        except Exception:
             self.SAGEMAKER_ENDPOINT_NAME = "placeholder-sagemaker-endpoint"

settings = Settings()
