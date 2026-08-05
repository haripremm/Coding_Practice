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
    (103,"Ravi", "ravi@gmail.com", 9675234553,"ECE",18000,"2025-08-22"),
    (104,"Vijay", "Vijay@gmail.com", 9687323453,"CSE",52000,"2021-08-20"),
    (105,"Ajith", "Ajith@gmail.com", 9675282573,"EEE",111000,"2016-07-12"),
    (106,"Kumar", "kumar@gmail.com", 9623434593,"ECE",12500,"2025-05-22")
    ]

cursor.executemany(value,Detail)

mydb.commit()

cursor.execute('Select * from Employee_Management')

result=cursor.fetchall()

for i in result:
    print(i)

#print("Inserted Sucessfully")



