
try:
    prompt = int(input("Guess a number between 10 and 30:\n"))
    if prompt == 23:
        print("Good guess")
    elif prompt > 15 and prompt < 23:
        print("Number is lower than expected")
    elif prompt < 10:
        print("Guess is too low.")
    elif prompt > 23 and prompt < 30:
        print("Guess is higher than expected.")
    else:
        exit
except ValueError:
    print("Please enter a number")
                