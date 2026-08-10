import csv

employees =[ [1,"Arun","IT", 50000],
             [2,"Priya","HR", 45000 ],
             [3,"Kumar","Finance",60000]]

with open("Employees.csv","w", newline="") as file:
    writer = csv.writer(file)
    writer. writerow(["id","Name", "Department", "Salary"])
    writer.writerows(employees)
