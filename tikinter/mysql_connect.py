import mysql.connector
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
    )
    cursor = connection.cursor() 
    sql= "CREATE DATABASE IF NOT EXISTS Sneha"
    cursor.execute(sql)
    print("Database created successfully")

except mysql.connector.Error as err:
    print(f"error: '{err}'")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
       
