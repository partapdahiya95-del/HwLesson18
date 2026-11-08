def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
print("FUNCTION CALCULATOR")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    op = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()

    if op == "add":
        print("Result:", add(num1, num2))
    elif op == "subtract":
        print("Result:", subtract(num1, num2))
    elif op == "multiply":
        print("Result:", multiply(num1, num2))
    elif op == "divide":
        print("Result:", divide(num1, num2))
    else:
        print("Unknown operation.")

except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Thank you for using the calculator!")