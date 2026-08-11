#Json file creation
import json

data ={
    "Name":"Hari",
    "Age": 23,
    "City":"TKM"
}

with open("mydata.json","w") as f:
    json.dump(data,f,indent=4)

print("Json File Created")

#Updation IN Json file

with open("mydata.json","r") as f:
    data = json.load(f)

data["Course"] ="Python"
data["Skill"] = ["Python", "Sql","Power bi", "Ms Office"]

with open("mydata.json","w") as f:
    json.dump(data, f, indent=4)

print("data added")