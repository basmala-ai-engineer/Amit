def get_valid_number(prompt):
    """Function to validate that the user inputs a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b


def calculator():
    while True:
        print("\n--- Basic Calculator ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Choose an operation (1-5): ").strip()

        if choice == "5":
            print("\nThank you for using the calculator! Goodbye.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please select a number from 1 to 5.")
            continue

        num1 = get_valid_number("Enter the first number: ")
        num2 = get_valid_number("Enter the second number: ")

        if choice == "1":
            result = add(num1, num2)
            print(f"\nThe result of adding {num1} and {num2} is {result}.")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"\nThe result of subtracting {num2} from {num1} is {result}.")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"\nThe result of multiplying {num1} and {num2} is {result}.")
        elif choice == "4":
            result = divide(num1, num2)
            if isinstance(result, str):
                print(f"\n{result}")
            else:
                print(f"\nThe result of dividing {num1} by {num2} is {result}.")

        another = (
            input("\nDo you want to perform another calculation? (yes/no): ")
            .strip()
            .lower()
        )
        if another != "yes":
            print("\nThank you for using the calculator! Goodbye.")
            break


calculator()