import os
import snowflake.connector
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

# Flatten JSON data and insert into another table
cursor = conn.cursor()
cursor.execute("""
    INSERT INTO flattened_table
    SELECT 
        value:key1::string AS key1,
        value:key2::int AS key2,
        value:key3::float AS key3
    FROM your_table,
    LATERAL FLATTEN(input => variant_column) AS flattened_data
""")

cursor.close()
conn.close()