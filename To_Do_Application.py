import json

# File to store tasks
TASKS_FILE = "tasks.txt"

# Function to load tasks from a file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to a file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" added successfully!')

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to show!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{i}. {task['task']} - {status}")

# Mark a task as complete
def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter the task number to mark as completed: "))
        tasks[task_no - 1]["completed"] = True
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number!")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter the task number to delete: "))
        removed_task = tasks.pop(task_no - 1)
        print(f'Task "{removed_task["task"]}" deleted successfully!')
    except (IndexError, ValueError):
        print("Invalid task number!")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
