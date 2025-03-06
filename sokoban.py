
def sokoban():
    history = []
    while True:
        action = input("Action: ")

        if action == "Undo":
            undone = history.pop()
            print(f"Undone: {undone}")
        elif action == "Restart":
            restart = history.clear()
        else:
            history.append(action)
        print(history)

sokoban()