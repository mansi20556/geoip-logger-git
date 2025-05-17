import json
import requests
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('GeoLogsIP')  # Use your new table name here if changed

def lambda_handler(event, context):
    ip = event['requestContext']['http']['sourceIp']
    
    api_key = 'YOUR_API_KEY'  # Replace with your actual ipgeolocation.io API key
    response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip}")
    geo = response.json()
    
    request_id = str(uuid.uuid4())  # Unique ID for each record
    timestamp = datetime.utcnow().isoformat()  # Current UTC time in ISO format
    
    # Put unique item in DynamoDB
    table.put_item(Item={
        'request_id': request_id,
        'timestamp': timestamp,
        'ip': ip,
        'city': geo.get('city', 'N/A'),
        'state': geo.get('state_prov', 'N/A'),
        'country': geo.get('country_name', 'N/A'),
        'isp': geo.get('isp', 'N/A'),
    })

    clean_output = {
        'message': 'Logged!',
        'ip': ip,
        'city': geo.get('city', 'N/A'),
        'state': geo.get('state_prov', 'N/A'),
        'country': geo.get('country_name', 'N/A'),
        'isp': geo.get('isp', 'N/A')
    }

    return {
        'statusCode': 200,
        'body': json.dumps(clean_output, indent=2),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
