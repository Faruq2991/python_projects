students = {
    "Harry Potter": "Gryffindor",
    "Hermione Grenger": "Gryffindor",
    "Ron Wesaley": "Gryffindor",
    "Draco Malfoy": "Slytherin"
    
}

for student in students:
    print(student, students[student], sep=": ")


studs = [ # A list of dictionaries.
        {"name": "Harry", 
         "house": "Gryffindor", 
         "patronus": "Stag"},

        {"name": "Ron", 
         "house": "Gryffindor", 
         "patronus": "Jack terrier"},

        {"name": "Hermione", 
         "house": "Gryffindor", 
         "patronus": "Otter"},

        {"name": "Draco", 
         "house": "Slytherin", 
         "patronus": None}
]
for stud in studs:
    print(stud["name"],stud["house".strip()], stud["patronus"], sep="\t\t\t")



'''
students = ["Harry Potter", 
            "Hermione Grenger",
            "Ron Weasley", 
            "Draco Malfoy"

]

for student in range(len(students)):
    print(student + 1, students[student])

'''
