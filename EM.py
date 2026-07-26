import mysql.connector

mydb = mysql.connector.connect( 
    host = '127.0.0.1',
    user = 'root',
    password = 'Hari@080802',
)
cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Employee_Management")

print("Database Created Sucessfully")

cursor.close()

