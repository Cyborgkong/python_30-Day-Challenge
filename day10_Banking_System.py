import json
import os

FILE_PATH = 'json Projects/bank_data.json'

def load_data():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]['password'] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid credentials.")
        return None

def check_balance(username):
    print(f"{username}'s balance is: {users[username]['balance']}")

def deposit(username, amount):
    users[username]['balance'] += amount
    print(f"{amount} deposited. New balance: {users[username]['balance']}")

def withdraw(username, amount):
    if users[username]['balance'] >= amount:
        users[username]['balance'] -= amount
        print(f"{amount} withdrawn. New balance: {users[username]['balance']}")
    else:
        print("Insufficient funds.")

def new_user():
    username = input("Enter new username: ")
    if username in users:
        print("Username already exists.")
    else:
        password = input("Enter new password: ")
        users[username] = {'password': password, 'balance': 0.00, 'transactions': []}
        save_data(users)
        print(f"User '{username}' created with balance 0.00.")

# Main Program
users = load_data()

while True:
    print("\nWelcome to the Bank System")
    print("1. Login")
    print("2. New User")
    print("3. Exit")
    
    main_choice = input("Enter choice: ")
    
    if main_choice == '1':
        logged_in_user = login()
        if logged_in_user:
            while True:
                print(f"\nHello {logged_in_user}! What would you like to do?")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Logout")
                
                user_choice = input("Enter choice: ")
                
                if user_choice == '1':
                    check_balance(logged_in_user)
                elif user_choice == '2':
                    amount = float(input("Enter amount: "))
                    deposit(logged_in_user, amount)
                    save_data(users)
                elif user_choice == '3':
                    amount = float(input("Enter amount: "))
                    withdraw(logged_in_user, amount)
                    save_data(users)
                elif user_choice == '4':
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Try again.")
    elif main_choice == '2':
        new_user()
    elif main_choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
