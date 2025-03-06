
side_1 = int(input("Side A: "))
side_2 = int(input("Side B: "))
side_3 = int(input("Side C: "))

if side_1 == side_2 == side_3:
    print("Equilateral")
elif side_1 == side_2 != side_3:
    print("Isosceles")
else:
    print("Scalene")
