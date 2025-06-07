import json
import os

FILE_PATH = 'json Projects/todo.json'

def load_data():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

def add_task():
    task = input("Add Task: ")
    store = {
        'task': task,
        'done': False
    }
    data = load_data()
    data.append(store)
    save_data(data)
    print(f"'{task}' added successfully.")

def view_tasks():
    data = load_data()
    if not data:
        print("No tasks found.")
        return
    print("\nTo-Do List:")
    for idx, store in enumerate(data, start=1):
        status = "✅ Done" if store['done'] else "❌ Not Done"
        print(f"{idx}. {store['task']} — {status}")

def mark_done():
    data = load_data()
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(data):
            data[index]['done'] = True
            save_data(data)
            print(f"Marked '{data[index]['task']}' as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Use a number.")

def delete_task():
    data = load_data()
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(data):
            removed = data.pop(index)
            save_data(data)
            print(f"Deleted '{removed['task']}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Use a number.")

def menu():
    while True:
        print("\n--- To-Do Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do App...")
            break
        else:
            print("Invalid choice. Try again.")

menu()