import csv

'''name = input("What's your name: ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
'''
names = []
with open("names.txt") as file:
    #lines = file.readlines()
    for line in sorted(file, reverse=True):
      print(f"hello, {line.rstrip()}")