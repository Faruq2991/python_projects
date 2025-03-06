import csv

students = []
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        students.append({"Name": row["Name"], "Age": row["Age"], "Grade": row["Grade"]})
print(students)