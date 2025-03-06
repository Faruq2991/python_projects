import time

try:
    timer = int(input("Enter wait time (in seconds): "))
    print(f"Waiting for {timer} seconds...")
    time.sleep(timer)
    print("Countdown Complete: Hurray! 🎉")
except ValueError:
    print("Invalid input! Please enter a numeric value.")
