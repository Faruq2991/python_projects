count = 0

number = [1,2,3,4,5,6,7,8,9,10]

for x in number:
    if x % 2 == 0:
        count += 1
        print(x,)
print("We have", count, "even numbers.")
