# Calculator App -- GUI

from decimal import Decimal, getcontext, InvalidOperation

# Set the precision
getcontext().prec = 28

# Arithmetic operation
def add(x, y):
    return Decimal(x) + Decimal(y)
def subtract(x, y):
    return Decimal(x) - Decimal(y)
def multiply(x, y):
    return Decimal(x) * Decimal(y)
def divide(x, y):
    if Decimal(y) == 0:
        raise ValueError("Cannot divide by zero")
    return Decimal(x) / Decimal(y)

# Main calculator function
def calculator():
    print ('Choose a mathematical operation:')
    print ('1. Addition')
    print ('2. Subtraction')
    print ('3. Multiplication')
    print ('4. Division')
    print ('Enter "q" at any point to quit application')


    while True:
        try:
            operation = input("Select operation 1,2,3,4 : ")
            if operation.lower() == 'q':
                break
            num1 = input("Enter first number: ")
            if num1.lower() == 'q':
                break
            num2 = input("Enter second number: ")
            if num2.lower() == 'q':
                break


            # Convert inputs to Decimal and perform the chosen operation
            try:
                num1 = Decimal(num1)
                num2 = Decimal(num2)
            except (ValueError, InvalidOperation):
                print("Invalid input. Please enter numeric values.")
                continue

            # Perform the chosen operation
            if operation == '1':
                result = add(num1, num2)
            elif operation == '2':
                result = subtract(num1, num2)
            elif operation == '3':
                result = multiply(num1, num2)
            elif operation == '4':
                result = divide(num1, num2)
            else:
                print("Invalid operation.")
                continue

            # Check if the result is a whole number and display accordingly
            if result == result.to_integral_value():
                print(f"Result: {int(result)}") # Display as an integer
            else:
                print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")

#Run the Calculator
calculator()


