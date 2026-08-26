#Electricity bill Calculator
try:
    unit = int(input("Enter Your Unit:"))
    price=0
except ValueError:
    print("Enter The Correct Value")

if unit <=200:
    print("Electricity Bill is Zero")
elif unit >201 or unit <400:
    price = unit - 200
    total=price*4.7
    print(f"Your Electricity Bill Is : {total}")
elif unit >401 or unit <500:
    price = unit - 200
    total=price * 6.3
    print(f"Your Electricity Bill Is : {total}")


