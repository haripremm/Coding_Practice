import os
from dotenv import load_dotenv
import mysql.connector 

load_dotenv()

mydb = mysql.connector.connect(
    host = os.getenv("mysql_host"),
    user = os.getenv("mysql_user"),
    password = os.getenv("mysql_password"),
    database = "Employee_Management"

)

cursor = mydb.cursor()

table = ("Create table IPL (Team Varchar (25), captain varchar(25))")
cursor.execute(table)

mydb.commit()




