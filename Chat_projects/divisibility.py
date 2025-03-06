
x = int(input("Enter a number: \n"))

if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")
if x % 3 == 0 and x % 5 != 0:
    print("Fizz")
if x % 3 != 0 and x % 5 == 0:
    print("Buzz")
else:
    print(x)
