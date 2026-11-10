# To-Do List Application

tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def complete_task():
    view_tasks()
    if tasks:
        num = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num] = "[Completed] " + tasks[num]
            print("Task marked complete.")
        else:
            print("Invalid task number.")

def delete_task():
    view_tasks()
    if tasks:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            del tasks[num]
            print("Task deleted.")
        else:
            print("Invalid task number.")

def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
