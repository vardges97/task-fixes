def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "cant divide by zero"
    return x / y

while True:
    print("\nMenu:")
    print("press 1 for Addition")
    print("press 2 for Subtraction")
    print("press 3 for Multiplication")
    print("press 4 for Division")
    print("press 5 for Exit")

    choice = input("Select an operation (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4'):
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        if not num1.isnumeric() or not num2.isnumeric():
            print("Both inputs must be numeric. Please try again.")
        else:
            num1 = float(num1)
            num2 = float(num2)

            if choice == '1':
                result = add(num1, num2)
                print("Result: ", result)
            elif choice == '2':
                result = subtract(num1, num2)
                print("Result: ", result)
            elif choice == '3':
                result = multiply(num1, num2)
                print("Result: ", result)
            elif choice == '4':
                result = divide(num1, num2)
                print("Result: ", result)
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5).")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != "yes":
        print("Exiting the calculator. Goodbye!")
        break