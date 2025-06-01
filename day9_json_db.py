import json
import os

FILE_PATH = 'users.json'

def load_data():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        return json.load(file)
    
def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

def add_user():
    name = input("Enter user's name: ")
    age = input("Enter user's age: ")
    email = input("Enter user's email: ")
    
    user = {
        'name': name,
        'age': age,
        'email': email
    }
    
    data = load_data()
    data.append(user)
    save_data(data)
    print(f"User {name} added successfully.")
    
def show_users():
    data = load_data()
    if not data:
        print("No user found.")
        return
    print("\nList of users: ")
    for user in data:
        print(f"Name: {user['name']}, Age: {user['age']}, Email: {user['email']}")

while True:
    print("\nMenu:")
    print("1. Add User")
    print("2. Show Users")
    print("3. Exit")
    
    choice = input("Enter choice (1 - 3): ")
    
    if choice == '1':
        add_user()
    elif choice == "2":
        show_users()
    elif choice == "3":
        print("Exiting....")
        break
    else:
        print("Invalid choice. please try again.") 