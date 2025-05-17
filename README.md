# Project: GeoIP Logger (AWS Lambda + API Gateway + DynamoDB)

# Description
Capture and log visitor IP addresses with geo-location details using ipgeolocation.io API.
Stores logs in DynamoDB and returns a clean JSON response.

# Technologies Used
- AWS Lambda (Python)
- API Gateway (HTTP)
- DynamoDB
- ipgeolocation.io API

# DynamoDB Table
Table Name: GeoLogsIP
Partition Key: request_id (String)
Sort Key: timestamp (String)

# Lambda Function Logic
- Get IP from event['requestContext']['http']['sourceIp']
- Call ipgeolocation.io with API key and IP
- Log IP, city, state, country, ISP, timestamp, and request_id to DynamoDB
- Return minimal JSON in browser

# Sample Output
{
  "message": "Logged!",
  "ip": "106.219.147.100",
  "city": "New Delhi",
  "state": "Delhi",
  "country": "India",
  "isp": "airtel.com"
}

# Install Dependencies
pip install requests -t .

# Zip for Deployment
zip -r lambda-deploy.zip ./*

# Deploy Lambda
- Runtime: Python 3.12 or 3.13
- Upload lambda-deploy.zip
- Set env variable: API_KEY = your_ipgeolocation_api_key
- Assign IAM role with DynamoDB + CloudWatch permissions

# Create API Gateway
- HTTP API
- Connect to Lambda function
- Deploy and use URL in browser or on any device

# Notes
- Each log entry is unique using uuid + timestamp
- Prevents overwriting in DynamoDB
- Lightweight and free-tier friendly
