import json

def add_data():
    name = input("Enter your Name!:")
    Age = int(input("Enter your Age:"))
    course = input("Enter Your Course:")
    dept = input("Enter Your DEPT")
    collage = input("Enter your collage name:")

    Data = [{
        "Name":name,
        "Age" : Age,
        "Course" : course,
        "Dept" : dept,
        "Collage" : collage
    }]


    try:
        with open("Data.json","r") as f:
            datas = json.load(f)
    except FileNotFoundError:
        datas = []
    datas.append(Data)

    with open("Data.json","w") as f:
        json.dump(datas,f,indent=4)
    
    print("Data added sucessfully")


def view_data():
    
    with open("Data.json","r") as f:
        val = json.load(f)
    for i in val:
        print(i)
def main():
    choice = input("Enter your choice 1-2!:")
    if choice == "1":
        add_data()
    if choice == "2":
        view_data()
    



if __name__ == "__main__":
    main()


