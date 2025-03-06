
grade = int(input("Enter your grade: "))

if grade >= 90:
    print("Grade: A")
elif grade < 90 and grade >=80:
    print("Grade: B")
elif grade < 80 and grade >=70:
    print("Grade: C")
elif grade < 70 and grade >=60:
    print("Grade: D")
else:
    print("Grade: F")