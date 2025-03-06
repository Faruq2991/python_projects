


with open("notes.txt", "r") as f:
    lines = f.readlines()

    num_lines = len(lines)
    numb_words = sum(len(line.split()) for line in lines)
    numb_chars = sum(len(line) for line in lines)
    
print(numb_words)
print(num_lines)
print(numb_chars)