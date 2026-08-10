import csv

employees =[ [1,"Arun","IT", 50000],
             [2,"Priya","HR", 45000 ],
             [3,"Kumar","Finance",60000]]

with open("Employees.csv","r") as file:
    reader = csv.reader(file)

    for i in reader:
        print(i)
