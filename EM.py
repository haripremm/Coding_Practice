from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

mydb = mysql.connector.connect( 
    host = os.getenv("mysql_host"),
    user = os.getenv("mysql_user"),
    password =os.getenv("mysql_password"),
    database = "Employee_Management"
)
cursor = mydb.cursor()

table= """CREATE TABLE IF NOT EXISTS Employee_Management (
              Emp_Id INT AUTO_INCREMENT PRIMARY KEY,
              User_name vARCHAR(50) NOT NUll,
              Email varchar(50) Unique,
              Phone VarChar(50),
              Deparment varchar(15),
              salary decimal(10,2),
              Joining_date DATE );
"""
cursor.execute(table)
mydb.commit()

print("Table Created Sucessfully")

cursor.close()

