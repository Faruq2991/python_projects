
temps = [
    "1. Celsius to Fahrenheit",
    "2. Fahrenheit to Celsius"
]
for temp in temps:
    print(temp)

choice = input("Celsius to Fahrenheit or Fahrenheit to Celsius: ").strip().lower()

if choice == "1" or choice == "Celsius to Fahrenheit":
    try:
        prompt = float(input("Enter Temperature: "))
        f = prompt * 9/5 + 32
        print(f"{prompt}°C is {f}°F")
            
    except ValueError:
        print("Enter a Number Value.")

elif choice == "2" or choice == "Fahrenheit to Celsius":
    try:
        prompt = float(input("Enter Temperature: "))
        c = (prompt - 32) * 5/9
        print(f"{prompt}°F is {c}°C")
    except ValueError:
        print("Enter a Number Value.")
else:
    print("Invalid Input.")