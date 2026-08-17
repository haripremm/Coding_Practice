#calculator.py
def addition(a,b):
    add = a+b
    print(add)
def substraction(a,b): 
    sub = a-b
    print(sub)
def multiple(a,b):
    mul = a*b
    print(mul)
def division(a,b):
    div = a/b
    print(div)

def menu():
    print("********** MINI CALCULATOR *********")
    
    print()
    print("1.Addition!:")
    print("2.Substraction!:")
    print("3.Multiplication:")
    print("4. Division!:")
    print()
    op = int(input("Select Your Option!:"))   

    if op == 1:
        a= int(input("Enter the Number:"))
        b= int(input("Enter the  number:"))
        addition(a,b)
    elif op == 2:
        a= int(input("Enter the Number:"))
        b= int(input("Enter the  number:"))
        substraction(a,b)
    elif op == 3:
        a= int(input("Enter the Number:"))
        b= int(input("Enter the  number:"))
        Multiple(a,b)
    elif op == 4:
        a= int(input("Enter the Number:"))
        b= int(input("Enter the  number:"))
        division(a,b)
    else:
        print("Select option from 1-4")

if __name__ == "__main__":
     menu()


