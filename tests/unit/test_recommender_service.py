import pytest
import json
from unittest.mock import patch, MagicMock
from app.services.recommender_service import RecommenderService

class DummySettings:
    AWS_REGION = "us-east-1"
    SAGEMAKER_ENDPOINT_NAME = "test-endpoint"

@pytest.fixture
def recommender_service(mock_boto_client):
    with patch("app.services.recommender_service.settings", DummySettings()):
        return RecommenderService()

@pytest.mark.asyncio
async def test_get_recommendations_success(recommender_service, mock_boto_client):
    # Setup mock response from SageMaker
    mock_response_body = MagicMock()
    mock_response_body.read.return_value = json.dumps(["prod_1", "prod_2", "prod_3"]).encode('utf-8')
    mock_boto_client.invoke_endpoint.return_value = {"Body": mock_response_body}

    # Execute
    result = await recommender_service.get_recommendations("user_123", 3)

    # Assert
    assert result == ["prod_1", "prod_2", "prod_3"]
    mock_boto_client.invoke_endpoint.assert_called_once()
    call_args = mock_boto_client.invoke_endpoint.call_args[1]
    assert call_args["EndpointName"] == "test-endpoint"
    assert json.loads(call_args["Body"]) == {"user_id": "user_123", "num_recommendations": 3}

@pytest.mark.asyncio
async def test_get_recommendations_missing_endpoint(recommender_service):
    with patch("app.services.recommender_service.settings.SAGEMAKER_ENDPOINT_NAME", ""):
        with pytest.raises(Exception) as exc_info:
            await recommender_service.get_recommendations("user_123", 5)
        
        assert str(exc_info.value) == "SageMaker endpoint not configured"
