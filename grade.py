
def computegrade(score):
    score = float(input("Enter a Grade: \n"))
    if score >= 0.9:
        print("A")
    elif score <= 0.9 and score >= 0.8:
        print("B")
    elif score <= 0.8 and score >= 0.7:
        print("C")
    elif score <= 0.7 and score >= 0.6:
        print("D")
    elif score <= 0.6 and score >= 0.5:
        print("E")
    else:
        print("F")

    if type(score) != float:
        print("Bad score")
computegrade(100)
