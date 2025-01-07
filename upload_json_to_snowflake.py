import os
import snowflake.connector
import boto3
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Snowflake connection parameters
conn = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account=os.getenv('SNOWFLAKE_ACCOUNT'),
    warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
    database=os.getenv('SNOWFLAKE_DATABASE'),
    schema=os.getenv('SNOWFLAKE_SCHEMA')
)

# S3 bucket details
s3_bucket = os.getenv('AWS_S3_BUCKET')
s3_key = os.getenv('AWS_S3_KEY')

# Initialize S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

# Download JSON data from S3
response = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
json_data = json.loads(response['Body'].read().decode('utf-8'))

# Convert JSON data to string
json_data_str = json.dumps(json_data)

# Insert JSON data into Snowflake table
cursor = conn.cursor()
cursor.execute("""
    INSERT INTO your_table (variant_column)
    SELECT PARSE_JSON(%s)
""", (json_data_str,))

cursor.close()
conn.close()