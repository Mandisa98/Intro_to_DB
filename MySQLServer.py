import mysql.connector
from mysql.connector import Error

try:
    # Try to connect to MySQL server (change 'root' and 'your_password' to your own details)
    connection = mysql.connector.connect(
        host='localhost',         # This means it's running on your computer
        user='root',              # The username (often 'root')
        password='Mandisa-1998'  # Replace with your actual MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Always close the connection to avoid memory leaks
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
