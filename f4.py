balance = 50000
def deposit():
    amount = int(input("Enter the amount:"))
    
    if amount<0:
        print("Please Enter The Valid amount:")
    else:
        balance = balance + amount
        print("Your Cash Deposit Sucesssfully")

def Withdraw():
    amount = int(input("Enter the Cash amount to Withdraw:"))
    if amount < 0:
        print("Please Enter the valid amount")
    elif amount > balance:
        print("Your Account not have Enough Balance")
    else:
        balance = balance - amount
        print("Your Balance is: {balance}")

def menu():
    print("Enter  your Option")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")

    Choice = int(input("Enter Your Choice: From 1 - 4  :"))

    if Choice == "1":
        deposit()
    elif Choice== "2":
        Withdraw()

if __name__ =="__main__":
    menu()

        
            