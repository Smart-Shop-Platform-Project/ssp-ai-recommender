import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

@pytest.fixture(scope="module")
def client():
    return TestClient(app)

@pytest.fixture(scope="function")
def mock_boto_client():
    with patch("app.services.recommender_service.boto3.client") as mock_boto:
        mock_sagemaker = MagicMock()
        mock_boto.return_value = mock_sagemaker
        yield mock_sagemaker
