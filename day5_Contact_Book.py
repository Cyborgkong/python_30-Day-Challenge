print("Welcome to Contact Book!")
contacts = {}

while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(f"Contact {name} added.")
    elif choice == '2':
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name}'s phone number is {contacts[name]}")
        else:
            print("Contact not found.")
    elif choice == '3':
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print(f"{name}'s contact updated.")
        else:
            print("Contact not found.")
    elif choice == '4':
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"{name} has been deleted.")
        else:
            print("Contact not found.")
    elif choice == '5':
        if contacts:
            print("Contact list:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-6.")