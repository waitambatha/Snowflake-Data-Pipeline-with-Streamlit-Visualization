import os
import snowflake.connector
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch JSON data directly from the URL
url = "https://data.ny.gov/api/views/5xaw-6ayf/rows.json?accessType=DOWNLOAD"
response = requests.get(url)
json_data = response.json()

# Extract column names from the meta.view.columns field
column_names = [col["name"] for col in json_data.get("meta", {}).get("view", {}).get("columns", [])]

# Extract the data rows from the JSON
data_rows = json_data.get("data", [])

# Infer schema from the first row of data
if data_rows:
    first_row = data_rows[0]
    schema = []
    for i, value in enumerate(first_row):
        column_name = column_names[i] if i < len(column_names) else f"column_{i}"  # Use column names from JSON or fallback to generic names
        column_type = "VARCHAR"  # Default to VARCHAR for simplicity
        schema.append((column_name, column_type))

# Snowflake connection parameters
conn = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account=os.getenv('SNOWFLAKE_ACCOUNT'),
    warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
    database=os.getenv('SNOWFLAKE_DATABASE'),
    schema=os.getenv('SNOWFLAKE_SCHEMA'),
    insecure_mode=True  # Disables SSL verification (for testing only)
)

# Create the table dynamically
table_name = "dynamic_table"
create_table_sql = f"CREATE OR REPLACE TABLE {table_name} ("
create_table_sql += ", ".join([f'"{col_name}" {col_type}' for col_name, col_type in schema])  # Use double quotes for column names
create_table_sql += ")"

cursor = conn.cursor()
cursor.execute(create_table_sql)
print(f"Table '{table_name}' created successfully with columns: {', '.join([col_name for col_name, _ in schema])}")

# Insert data into the table
insert_sql = f"INSERT INTO {table_name} VALUES ("
insert_sql += ", ".join(["%s"] * len(schema))
insert_sql += ")"

for row in data_rows:
    cursor.execute(insert_sql, row)

cursor.close()
conn.close()

print("Data loaded into Snowflake successfully!")