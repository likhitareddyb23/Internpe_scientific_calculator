import math

def calculator():
    print("Scientific Calculator")

    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Square Root")
        print("7. Logarithm (base 10)")
        print("8. Sine")
        print("9. Cosine")
        print("10. Tangent")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            print("Calculator is shutting down...")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = num1 + num2
            print("Result: ", result)
        elif choice == '2':
            result = num1 - num2
            print("Result: ", result)
        elif choice == '3':
            result = num1 * num2
            print("Result: ", result)
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print("Result: ", result)
            else:
                print("Error: Division by zero")
        elif choice == '5':
            result = math.pow(num1, num2)
            print("Result: ", result)
        elif choice == '6':
            result = math.sqrt(num1)
            print("Result: ", result)
        elif choice == '7':
            result = math.log10(num1)
            print("Result: ", result)
        elif choice == '8':
            result = math.sin(math.radians(num1))
            print("Result: ", result)
        elif choice == '9':
            result = math.cos(math.radians(num1))
            print("Result: ", result)
        elif choice == '10':
            result = math.tan(math.radians(num1))
            print("Result: ", result)
        else:
            print("Invalid choice. Try again.")

# Start the calculator
calculator()
