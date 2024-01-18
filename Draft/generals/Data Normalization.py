import pandas as pd
import psycopg2
import re
from sqlalchemy import create_engine

# Replace the following with your database connection details
db_params = {
    "host": "localhost",
    "database": "Skyloov",
    "user": "postgres",
    "password": "Skyloov@123",
    "port": "5401",
}

connection = psycopg2.connect(**db_params)

# Replace the SQL query with your actual query
sql_query = """SELECT * FROM "AgencyData"."SalesForce_Data_V1";"""

df = pd.read_sql(sql_query, connection)

# Assuming 'Agency_Name' column exists in your DataFrame df
df['Agency'] = df['Agency_Name'].str.extract(r'(.*?)(real|property|properties)', flags=re.IGNORECASE)[0].str.strip()

# For agencies not containing "real", "property", or "properties"
df['Agency'] = df.apply(lambda row: row['Agency_Name'] if pd.isnull(row['Agency']) else row['Agency'], axis=1)

# Display DataFrame information
print(df[['Agency_Name', 'Agency']].info())

# Display DataFrame information
print(df[['Agency_Name', 'Agency']].head(50))

# Assuming 'Agency_Name' column exists in your DataFrame df
duplicates = df['Agency'][df['Agency'].duplicated(keep=False)]
duplicate_counts = duplicates.value_counts()

# Display duplicate strings and their counts
print("Duplicate Strings and Counts:")
print(duplicate_counts)

# Assuming 'Agency' column exists in your DataFrame df
df = df.drop_duplicates(subset=['Agency'], keep='first')

# Display DataFrame information
print("DataFrame Information (After Removing Duplicates):")
print(df[['Agency_Name', 'Agency']].info())

# Duplicate values and their counts in 'Agency' column after removing duplicates
duplicates_after_remove = df['Agency'][df['Agency'].duplicated(keep=False)]
duplicates_counts_after_remove = duplicates_after_remove.value_counts()

# Display duplicate values and their counts after removing duplicates
print("Duplicate Values and Counts (After Removing Duplicates):")
print(duplicates_counts_after_remove)

# Display DataFrame information
print(df[['Agency_Name', 'Agency']].head(50))

# Set the export file path
export_file_path = r"C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Agency_Data_Collecting\Data Comparison\cleaned_agency_data.csv"

# Export the cleaned DataFrame t    o a CSV file
df.to_csv(export_file_path, index=False)
print(f"DataFrame exported to: {export_file_path}")

# Close the database connection
connection.close()
