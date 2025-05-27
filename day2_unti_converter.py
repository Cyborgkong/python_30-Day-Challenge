def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(mi):
    return mi / 0.621371

def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(lb):
    return lb / 2.20462

while True:
    print("\nSelect conversion type:")
    print("1. Temperature")
    print("2. Distance")
    print("3. Weight")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

    if choice == '4':
        print("Goodbye!")
        break

    if choice == '1':
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        sub_choice = input("Enter choice: ").strip()

        value = float(input("Enter value: "))
        if sub_choice == '1':
            print(f"{value}°C = {celsius_to_fahrenheit(value):.2f}°F")
        elif sub_choice == '2':
            print(f"{value}°F = {fahrenheit_to_celsius(value):.2f}°C")
        else:
            print("Invalid choice")

    elif choice == '2':
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        sub_choice = input("Enter choice: ").strip()

        value = float(input("Enter value: "))
        if sub_choice == '1':
            print(f"{value} km = {kilometers_to_miles(value):.2f} miles")
        elif sub_choice == '2':
            print(f"{value} miles = {miles_to_kilometers(value):.2f} km")
        else:
            print("Invalid choice")

    elif choice == '3':
        print("1. Kilograms to Pounds")
        print("2. Pounds to Kilograms")
        sub_choice = input("Enter choice: ").strip()

        value = float(input("Enter value: "))
        if sub_choice == '1':
            print(f"{value} kg = {kilograms_to_pounds(value):.2f} lbs")
        elif sub_choice == '2':
            print(f"{value} lbs = {pounds_to_kilograms(value):.2f} kg")
        else:
            print("Invalid choice")

    else:
        print("Invalid choice. Please select 1-4.")
