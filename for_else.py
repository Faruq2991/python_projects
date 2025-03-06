
succesful = False

for number in range(1, 6):
    print("Attempt", number)
    if succesful:
        print("Message Sent!")
        break
else:
    print("Attempt Failed after", number, "tries.")