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

value = " Insert into Employee_Management(Emp_id, User_name, Email, Phone, deparment, salary,  Joining_date) Values (%s,%s,%s,%s,%s,%s,%s)"

Detail = [
    (101,"Hari", "hari@gmail.com", 967535853,"ECE",17000, "2025-02-13"),
    (102,"Prasath", "prasath@gmail.com", 967523453,"ECE",17000,"2025-06-22") 
    ]

cursor.executemany(value,Detail)

mydb.commit()

print("Inserted Sucessfully")