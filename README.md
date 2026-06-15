# SSP AI Recommender Service

This service provides personalized product recommendations using a machine learning model deployed on Amazon SageMaker. It is built using FastAPI and deployed as an AWS Lambda function using Mangum.

## Architecture
- **Framework:** FastAPI
- **Deployment:** AWS Lambda (Container Image)
- **Integration:** Amazon SageMaker Runtime
- **Secrets:** AWS Systems Manager (SSM) Parameter Store

## Prerequisites
- Python 3.12
- An active Amazon SageMaker endpoint for recommendations.
- The SageMaker endpoint name must be stored in AWS SSM Parameter Store.

## Local Development
1. Create a virtual environment: `python3 -m venv venv`
2. Activate it: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt` and `pip install -r requirements-dev.txt`
4. Set the `AWS_REGION` and `SAGEMAKER_ENDPOINT_NAME` environment variables (or rely on the SSM fallback logic if configured locally).
5. Run the application: `uvicorn app.main:app --reload`
