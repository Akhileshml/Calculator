def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def calculator():
    print("Simple Calclator ")
    print("Select operation:")
    print("1. Adda")
    print("2. Subtractt")
    print("3. Multiplyy")
    print("4. Divide")

    try:
        choice = int(input("Enter choice (1/2/3/4): "))
        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print(f"The result is: {add(num1, num2)}")
            elif choice == 2:
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == 3:
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == 4:
                print(f"The result is: {divide(num1, num2)}")
        else:
            print("Invalid input. Please choose a valid operation.")

    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    calculator()
