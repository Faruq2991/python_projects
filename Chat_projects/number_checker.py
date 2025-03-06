numb = int(input("Enter Number: "))
try:
    if numb > 0:
        print(f"{numb} is a positive number")
    elif numb < 0:
        print(f"{numb} is a negative number")
    else:
        print(f"{numb} is Zero")
except:
    print(f"{numb} is an invalid entry. Check and try again.")