
"""
To-Do List App (Advanced Version)
Start the program
Display a menu with options: Add Task, Remove Task, View Tasks, Exit
If "Add Task":
Ask the user for a task and store it in a list
If "Remove Task":
Show the list of tasks with numbers
Ask the user to enter the task number to remove
If "View Tasks":
Display all tasks
Repeat until the user chooses "Exit"
End

"""
def main():
    task_add = []  # List to store tasks

    while True:
        menu = [
            "1. Add Task",
            "2. Delete Task",
            "3. View Tasks",
            "4. Exit"
        ]
        
        for item in menu:
            print(item)

        prompt = input("Select Option: ").strip().lower()

        # Add a task
        if prompt == "1" or prompt == "add task":
            add = input("Enter a Task: ")
            task_add.append(add)
            print("Task Added Successfully!\n")

        # Delete a task
        elif prompt == "2" or prompt == "delete task":
            if task_add:
                print("\nAll Tasks:")
                for idx, task in enumerate(task_add, start=1):
                    print(f"{idx}. {task}")

                try:
                    task_num = int(input("\nEnter the number of the task to delete: "))
                    if 1 <= task_num <= len(task_add):
                        removed_task = task_add.pop(task_num - 1)
                        print(f"Deleted task: {removed_task}\n")
                    else:
                        print("Invalid task number. Please try again.\n")
                except ValueError:
                    print("Invalid input! Please enter a number.\n")
            else:
                print("No tasks available.\n")

        # View tasks
        elif prompt == "3" or prompt == "view tasks":
            if task_add:
                print("\nHere are all your tasks:")
                for idx, task in enumerate(task_add, start=1):
                    print(f"{idx}. {task}")
                print()  # Blank line for readability
            else:
                print("No tasks available.\n")

        # Exit program
        elif prompt == "4" or prompt == "exit":
            print("Exiting program. Goodbye!")
            break  # Exit the loop

        else:
            print("Invalid option. Please try again.\n")

# Run the program
main()
