units = int(input("Enter Your Units:"))
bill = 0

max_unit =500

if units < 500:
    max_unit=200
    if units <=200:
        bill =0
    elif units <=400:
        bill = (units-200) * 4.7
    else:
        bill = (units-200) * 6.3

print()
print("****** YOUR ELECTRICITY BILL *****")

print(f"Units Comsumed: {units} ")
print(f"Electricity Bill: {round(bill,2)}")
