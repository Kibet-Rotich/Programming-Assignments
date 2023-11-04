class Calculator:
    def __init__(self):
        pass
    def add(self, num1, num2):
        return num1 + num2  # Method for addition

    def subtract(self, num1, num2):
        return num1 - num2  # Method for subtraction

    def multiply(self, num1, num2):
        return num1 * num2  # Method for multiplication

    def divide(self, num1, num2):
        if num2 == 0:
            return "Cannot divide by zero"  # Method for division, checks for division by zero
        return num1 / num2

if __name__ == "__main__":
    calculator = Calculator()  # Create an instance of the Calculator class

    while True:
        print("Options:")
        print("Enter '1' for addition")
        print("Enter '2' for subtraction")
        print("Enter '3' for multiplication")
        print("Enter '4' for division")
        print("Enter '5' to end the program")

        operation = input(": ")  # Get user's choice

        print("********************************\n")

        if operation == "5":
            break  # Exit the program if the user enters '5'
        elif operation in ["1", "2", "3", "4"]:
            num1 = float(input("Enter first number: "))  # Get the first number from the user
            num2 = float(input("Enter second number: "))  # Get the second number from the user

            if operation == "1":
                print("Result: " + str(calculator.add(num1, num2)))  # Perform addition and display the result
            elif operation == "2":
                print("Result: " + str(calculator.subtract(num1, num2)))  # Perform subtraction and display the result
            elif operation == "3":
                print("Result: " + str(calculator.multiply(num1, num2)))  # Perform multiplication and display the result
            elif operation == "4":
                print("Result: " + str(calculator.divide(num1, num2)))  # Perform division and display the result
        else:
            print("Invalid input")  # Handle invalid input

        print("********************************\n")
