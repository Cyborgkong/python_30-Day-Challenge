import json
import os

FILE_PATH = 'json Projects/bank_data.json'

def load_data():
    if not os.path.exists(FILE_PATH):
        return {}  # Return dict instead of list
    with open(FILE_PATH, 'r') as file:
        return json.load(file)
    
def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)
        
def check_balance(name):
    if name in users:
        print(f"{name}'s balance is: {users[name]['balance']}")
    else:
        new_user(name)
        
def deposit(name, amount):
    if name in users:
        users[name]['balance'] += amount
        print(f"{amount} deposited. New balance: {users[name]['balance']}.")
    else:
        print("User not found.")
        
def withdraw(name, amount):
    if name in users:
        if users[name]['balance'] >= amount:
            users[name]['balance'] -= amount
            print(f"{amount} withdrawn. New balance: {users[name]['balance']}.")
        else:
            print("Insufficient funds.")
    else:
        print("User not found.")
        
def new_user(name):
    print(f"User '{name}' not found.")
    sign_up = input("Do you want to sign up? (y/n): ")
    if sign_up.lower() == 'y':
        users[name] = {'balance': 0.00}
        save_data(users)
        print(f"User '{name}' created with balance 0.00.")
    else:
        print("Sign-up cancelled.")

     
users = load_data()   
save_data(users)

while True:
    print("\nMenu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. New User")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        name = input("Enter user name: ")
        check_balance(name)
    elif choice == '2':
        name = input("Enter user name: ")
        amount = float(input("Enter amount: "))
        deposit(name, amount)
        save_data(users)
    elif choice == '3':
        name = input("Enter user name: ")
        amount = float(input("Enter amount: "))
        withdraw(name, amount)
        save_data(users)
    elif choice == '4':
        name = input("Enter new username: ")
        new_user(name)
    elif choice == '5':
        print("Exiting....")
        break
    else:
        print("Invalid choice. Try again")
