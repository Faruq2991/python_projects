N = int(input("Enter a number: "))

if N < 2:
    print("Composite")
else:
    is_prime = True
    for i in range(2, int(N ** 0.5) + 1):  # Checking up to sqrt(N) for efficiency
        if N % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Composite")