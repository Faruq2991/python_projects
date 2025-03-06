
def main():
    x = int(input("Enter a number: \n"))
    if is_even(x) == True:
        print(f"{x} is an even number.")
    else:
        print(f"{x} is an odd number.")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()
