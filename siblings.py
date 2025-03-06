import csv

with open("siblings.csv") as file:
    for line in file:
        name, position = line.rstrip().split(",")
        print(f"{name} {position}")