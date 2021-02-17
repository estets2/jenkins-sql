import os
import psycopg2
from psycopg2 import Error

POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASS = os.environ.get('POSTGRES_PASS')

try:
    # Connect to an existing database
    connection = psycopg2.connect(user=POSTGRES_USER,
                                  password=POSTGRES_PASS,
                                  host=POSTGRES_HOST,
                                  port="5432",
                                  database="docker")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")