"""
Start the program
Display a menu: Add Task, View Tasks, Exit
If "Add Task":
Ask the user to enter a task
Store the task in a list
If "View Tasks":
Display all tasks
Repeat until the user chooses "Exit"
End

"""
def main():
    task_add = []

    while True:
        menu = [
            "1. Add Task",
            "2. View Task",
            "3. Exit"
        ]
        for items in menu:
            print(f"{items}")
        
        prompt = input("select Option: ").lower().strip()

        if prompt == "1" or prompt == "add task":
            add = input("Enter a Task: ")
            task_add.append(add)
            print("Task Added Successfully")

        elif prompt == "2" or prompt == "view task":
            if task_add:
                print("Here are all your tasks:")
                for idx, task in enumerate(task_add, start=1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks available.\n")

        elif prompt == "3" or prompt == "exit":
            print("Exiting program. Goodbye!")
            break  # Exit the loop

        else:
            print("Invalid option. Please try again.\n")

main()