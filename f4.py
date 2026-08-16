try:
    name = input("Enter the Name: ")
    born_year = int(input("Enter the year:"))
    age = 2026 - born_year
    print("You Are" , name, "and Your Age:", age)
except TypeError:
    print("Enter a Valid input!")
except ValueError:
    print("Enter a Valid input!")
except ZeroDivisionError:
    print("Enter a Valid input!")

