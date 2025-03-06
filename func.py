
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome to Python programming")

greet("Umar", "Faruq")

def main():
    x = int(input("Enter X: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()
