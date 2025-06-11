import mysql.connector
from mysql.connector import Error

from .constants import DB_PASS, DB_USER, DB_HOST, DB_NAME

try:
    connection = mysql.connector.connect(
        host=DB_HOST,
        port=3306,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )

    if connection.is_connected():
        print("Successfully connected to the database")

        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("Connected to database:", record)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
