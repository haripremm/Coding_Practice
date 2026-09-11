'''from fastapi import FastAPI 

app = FastAPI()

@app.get("/")

def read):
    return {" Hello":"World"}

@app.get("/Items/{item_id}")

def read_item(item_id:int,q:str):'''

#***** ADDRESS VALIDATOR *****

def addressVal(address):
    dot = address.find(".")
    at = address.find("@")

    if (dot !=-1) and (at != -1):
        print(f"{address} is a Valid Email")
    else:
        print(f"{address} is a InValid Email")

print(" To Verify the valid Email....")

while(True):
    print("To Verify a Valid Email addess needs an @ and '.' Symbol ")

    x = input("Enter Your Email address: ")
    break

    addressVal(x)
   
    