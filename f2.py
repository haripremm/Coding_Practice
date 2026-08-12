import json

name = input("Enter the name:")
course = input("Enter your  course:")
dept = input("Enter your dept:")
Age = input("Enter your Age:")

details = {
    "Name" :name,
    "Course" : course,
    "Department" : dept,
    "Age" : Age
}

with open("St_Details.json", "w") as f:
    json.dump(details,f,indent=4)

with open("St_Details.json", "r") as f:
    detail =(json.load(f))
print(detail)




