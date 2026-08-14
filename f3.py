import json
import os

def add_data():
    name = input("Enter the name:")
    course = input("Enter your  course:")
    dept = input("Enter your dept:")
    Age = input("Enter your Age:")

    data = {
        "Name" : name,
        "Course" : course,
        "AGE" : Age,
        "DEPT" : dept
    }

    data_list = []

    if os.path.exists("Data.json"):
        with open("Data.json", "r") as f:
            try:
                data_list = data.load(f)
            except json.JSON.DecodeError:
                data_list = []
    data_list.append(data)

def view_data():
    try:
        if os.path.exists("Data.json"):
            with open("Data.json",'r') as f:
                 view = json.load(f)
                 for i in view:
                    print(i)
        else:
            print("Data Not Found Please select Option 1")
            print()
    except FileNotFoundError:
        print("Data Not Found Please Add User Data")
    #except json.JSONDecodeError


def main():
    while True:
        print("*"*30)
        print("        Welcome To user Data         ")
        print("*"*30)
        print("1. Add My Data:")
        print("2.Viwe My Data:")
        print("3.Exit")
        print()
        op = input("Enter your option:")
        if op == "1":
            add_data()
        elif op == "2":
            view_data()
        elif op =="3":
            break
        else:
            print("Enter a valid input:")

if __name__ =="__main__":
    main()


    



