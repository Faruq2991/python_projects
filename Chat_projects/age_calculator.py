from datetime import date

current_year = date.today().year
def main():

    prompt = int(input("Enter Birth Year: "))
    age = current_year - prompt
    print(f"You are {age} years old.")

main()
    


