WORDS = {
  "PAIR": 4,
  "HAIR": 4,
  "CHAIR": 5,
  "GRAPHIC": 7
 }

def spelling_bee():
    print(f"Welcome to WORDS TODAY")
    print(f"Your Letters are: G I P A R C H")
    score = 0
    while len(WORDS) > 0:
        print(f"{len(WORDS)} Words left.")
        guess = input("Guess a word: ")
        if guess == "GRAPHIC":
            print(f"BOOOOOMMMMM. Power Word")
            #print(f"{guess}. You scored {points}*2 points.")
        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"{guess}. You scored {points} points.")
            score += points
        
        print(f"Your score is: {score}")

spelling_bee()