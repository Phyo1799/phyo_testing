import pandas as pd
import psycopg2
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

print(df.head())
print(df.describe())
print(df.isnull().sum())

import matplotlib.pyplot as plt
import seaborn as sns


