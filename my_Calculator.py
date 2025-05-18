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
    return x ** y

def modulo(x, y):
    return x % y

def square_root(x):
    if x < 0:
        return "Error: Cannot take square root of a negative number"
    return x ** 0.5

# LOOPING FOR CONTINUOUS USE
while True:
    # MENU
    print("\nSelect operation:")
    print("+ for addition")
    print("- for subtract")
    print("* for multiplication")
    print("/ for division")
    print("^ for Power")
    print("'%' for Modulo")
    print("sqrt for Square Root")
    print("exit to quit")
    print("Exit to quit")

    choice = input("Enter operator symbol (+, -, *, /) or type 'exit': ").strip()

    if choice == 'exit':
        print("Goodbye!")
        break

    # COLLECTING NUMBER INPUT
    if choice in ['+', '-', '*', '/']:
        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue

        # CALLING CORRECT FUNCTION
        if choice == '+':
            print("Result:", add(num1, num2))
        elif choice == '-':
            print("Result:", subtract(num1, num2))
        elif choice == '*':
            print("Result:", multiply(num1, num2))
        elif choice == '/':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid symbol. Please use +, -, *, / or type 'exit'.")