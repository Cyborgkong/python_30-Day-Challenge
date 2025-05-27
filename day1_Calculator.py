# DEFINING THE MATH FUNCTIONS
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Cannot Divide by Zero (0)"
    return x / y


def power(x, y):
    return x**y


def modulo(x, y):
    return x % y


def square_root(x):
    if x < 0:
        return "Error: Cannot take square root of a negative number"
    return x**0.5


# HISTORY LIST
history = []

# LOOPING FOR CONTINUOUS USE
while True:
    # MENU
    print("\nSelect operation:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    print("^ for power")
    print("% for modulo")
    print("sqrt for square root")
    print("history to view previous calculations")
    print("exit to quit")

    choice = (
        input("Enter operator symbol (+, -, *, /, ^, %, sqrt) or type 'exit': ")
        .strip()
        .lower()
    )

    if choice == "exit":
        print("Goodbye!")
        break

    elif choice == "history":
        if not history:
            print("No calculations yet.")
        else:
            print("\nCalculation History:")
            for entry in history:
                print(entry)
        continue

    # BINARY OPERATIONS
    if choice in ["+", "-", "*", "/", "^", "%"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if choice == "+":
            result = add(num1, num2)
        elif choice == "-":
            result = subtract(num1, num2)
        elif choice == "*":
            result = multiply(num1, num2)
        elif choice == "/":
            result = divide(num1, num2)
        elif choice == "^":
            result = power(num1, num2)
        elif choice == "%":
            result = modulo(num1, num2)

        print("Result:", result)
        history.append(f"{num1} {choice} {num2} = {result}")

    # UNARY OPERATION (square root)
    elif choice == "sqrt":
        try:
            num = float(input("Enter number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        result = square_root(num)
        print("Result:", result)
        history.append(f"√{num} = {result}")

    else:
        print("Invalid symbol. Please use +, -, *, /, ^, %, sqrt or type 'exit'.")