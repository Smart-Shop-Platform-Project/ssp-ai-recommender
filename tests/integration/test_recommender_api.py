import pytest
from unittest.mock import patch, AsyncMock
from app.services.recommender_service import RecommenderService

def test_get_recommendations_api(client):
    with patch.object(RecommenderService, 'get_recommendations', new_callable=AsyncMock) as mock_get:
        mock_get.return_value = ["prod_A", "prod_B"]
        
        response = client.post(
            "/api/v1/recommendations?user_id=api_user_1&num_recommendations=2"
        )
        
        assert response.status_code == 200
        assert response.json() == ["prod_A", "prod_B"]
        mock_get.assert_called_once_with("api_user_1", 2)

def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "SSP AI Recommender is running"}
