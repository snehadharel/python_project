import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Sneha"
)

cursor = db_connection.cursor()

sql = """
    CREATE TABLE IF NOT EXISTS login(
    user VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL
    );
"""

cursor.execute(sql)
print("Table created successfully")
