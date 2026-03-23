import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks, description):
    """Add a new task."""
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'pending'
    }
    tasks.append(task)
    print(f"Task '{description}' added with ID {task_id}.")

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks found.")
        return
    print("\nTo-Do List:")
    print("-" * 30)
    for task in tasks:
        status = "[✓]" if task['status'] == 'done' else "[ ]"
        print(f"{task['id']}. {status} {task['description']}")
    print()

def mark_done(tasks, task_id):
    """Mark a task as done."""
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'done'
            print(f"Task {task_id} marked as done.")
            return
    print(f"Task with ID {task_id} not found.")

def delete_task(tasks, task_id):
    """Delete a task."""
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            removed_task = tasks.pop(i)
            print(f"Task '{removed_task['description']}' deleted.")
            # Reassign IDs
            for j in range(i, len(tasks)):
                tasks[j]['id'] = j + 1
            return
    print(f"Task with ID {task_id} not found.")

def main():
    """Main function to run the To-Do List application."""
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            description = input("Enter task description: ").strip()
            if description:
                add_task(tasks, description)
            else:
                print("Description cannot be empty.")
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            try:
                task_id = int(input("Enter task ID to mark as done: ").strip())
                mark_done(tasks, task_id)
            except ValueError:
                print("Invalid task ID.")
        elif choice == '4':
            view_tasks(tasks)
            try:
                task_id = int(input("Enter task ID to delete: ").strip())
                delete_task(tasks, task_id)
            except ValueError:
                print("Invalid task ID.")
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()