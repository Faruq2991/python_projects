import string
import random

def gen():

    prompt = int(input("Enter password length:\n"))

    '''This is a declarartion of all ASCII chars to be used in the program'''

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digit = string.digits
    char = string.punctuation
    
    # A list of all possible combinations

    combo = []
    combo.extend(list(upper))
    combo.extend(list(lower))
    combo.extend(list(digit))
    combo.extend(list(char))
    
    # Shuffle all combinations

    random.shuffle(combo)

    password = ("".join(combo[0:prompt]))

    print(password)

gen()