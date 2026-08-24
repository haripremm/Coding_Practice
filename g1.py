import csv

filename = "Student_data.csv"

with open(filename,"w",newline= '') as file:
    writer= csv.writer(file)

    writer.writerow(["Name","Age","Course","Dept"])

    while True:
        name = input("Enter your Name:")
        age = input("Enter Your Age:")
        course = input("Enter your Course:")
        dept = input("Enter Your Dept")

        writer.writerow([name,age,course,dept])

        choice = input("Do You Want to Add Another Student? (Y,N):").lower()

        if choice != "y":
            break
print("Data Added Sucessfully!")
        