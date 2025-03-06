import math

print("Add Subtract Multiply Divide")

def add():
    numb1 = int(input("Enter first number: "))

    numb2 = int(input("Enter second number: "))

    summ = numb1 + numb2

    print("Your answer is:",summ)

def sub():
    numb1 = int(input("Enter first number: "))

    numb2 = int(input("Enter second number: "))

    summ = numb1 - numb2

    print("Your answer is:",summ)

def mul():
    numb1 = int(input("Enter first number: "))

    numb2 = int(input("Enter second number: "))

    summ = numb1 * numb2

    print("Your answer is:",summ)

def div():
    numb1 = int(input("Enter first number: "))

    numb2 = int(input("Enter second number: "))

    summ = numb1 / numb2

    print("Your answer is:",summ)


choice = input("Select an operation to perform: \n")

if choice == "add":
    add()
elif choice == "sub":
    sub()
elif choice == "mul":
    mul()
elif choice == "div":
    div()
else:
    print("Invalid input.")

