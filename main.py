import os

task_file = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(task_file, 'w') as file:
        for task in tasks:
            file.write(task + "\n") 

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1): 
            print(f"{i}. {task}")

def add_task(tasks): 
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)

def remove_task(tasks):  
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number to remove: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)  # ✅ fixed variable name
                print(f"Task removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:  # ✅ loop moved inside main
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("👋 Exiting To-Do List App. Tasks saved!")
            break
        else:
            print("Invalid choice. Please select from 1-4.")

if __name__ == "__main__":
    main()
