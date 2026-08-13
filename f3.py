import json

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

    with open("Data.json", "w") as f:
        json.dump(data,f,indent=4)


def view_data():
    with open("Data.json",'r') as f:
       view = json.load(f)
       print(view)

def main():
    print("*"*10)
    print("1. Add My Data:")
    print("2.Viwe My Data:")
    print("*"*10)
    op = input("Enter your option:")

    if op == "1":
        add_data()
    elif op == "2":
        view_data()
    else:
        print("Enter a valid input:")
        main()


if __name__ =="__main__":
    main()


    



