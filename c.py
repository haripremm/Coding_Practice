from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

mydb = mysql.connector.connect(
    host =os.getenv("mysql_host"),
    user=os.getenv("mysql_user"),
    password=os.getenv("mysql_password"),
    database="Employee_management"
)

cursor = mydb.cursor()

cursor.execute("SElect * From Employee_Management")

data = cursor.fetchall()

for i in data:
    print(i)

