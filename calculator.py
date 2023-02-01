import unittest
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

def main():
    calculator = Calculator()
    while True:
        print("Choose the operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        choice = int(input("Enter your choice (1/2/3/4/5): "))

        if choice == 5:
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = calculator.add(num1, num2)
            print("Result:", result)
        elif choice == 2:
            result = calculator.subtract(num1, num2)
            print("Result:", result)
        elif choice == 3:
            result = calculator.multiply(num1, num2)
            print("Result:", result)
        elif choice == 4:
            result = calculator.divide(num1, num2)
            print("Result:", result)
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
    
