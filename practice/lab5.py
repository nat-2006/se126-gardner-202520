# Program: My Basic Calculator
# Description: This program provides a basic calculator with operations for addition, subtraction, multiplication, and division.
# Natalie Gardner
# 12/9/2024

def addition():
    """Add two numbers and return the result."""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1 + num2

def subtraction():
    """Subtract two numbers and return the result."""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1 - num2

def multiplication(a, b):
    """Multiply two numbers and display the result."""
    result = a * b
    print("The result of multiplying {} and {} is: {}".format(a, b, result))

def division():
    """Divide two numbers and return the result."""
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    if num2 != 0:
        return num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        return None

# Main program loop
print("Welcome to My Basic Calculator!")

choice = 0  # Initialize the variable to control the loop
while choice != 5:  # Continue until the user selects Exit
    # Display menu
    print("\nMenu:")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Exit")

    # Get user choice
    choice = int(input("Choose an option (1-5): "))

    if choice == 1:
        # Addition
        result = addition()
        print("The result is: {:.2f}".format(result))
    elif choice == 2:
        # Subtraction
        result = subtraction()
        print("The result is: {:.2f}".format(result))
    elif choice == 3:
        # Multiplication
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        multiplication(num1, num2)
    elif choice == 4:
        # Division
        result = division()
        if result is not None:
            print("The result is: {:.2f}".format(result))
    elif choice == 5:
        # Exit
        print("Thank you for using the calculator. Goodbye!")
    else:
        # Invalid input
        print("Invalid choice. Please select a valid option.")
