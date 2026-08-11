import json

data ={
    "Name":"Hari",
    "Age": 23,
    "City":"TKM"
}

with open("mydata.json","w") as f:
    json.dump(data,f,indent=4)

print("Json File Created")