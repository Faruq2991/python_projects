
def main():
    greeting = input("Greet: ").strip().lower()
    print(f"${get_greeting(greeting)}")

def get_greeting(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100
main()