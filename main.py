from calculator import add, subtract, multiply, divide, power, square_root

print("Welcome to the Calculator!")

while True:
    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "0":
        print("adiossss")
        break

    # Square root
    if choice == "6":
        num = float(input("Enter a number: "))
        result = square_root(num)
        print("Result: ", result)

    # All other operations need 2 numbers
    elif choice in ["1", "2", "3", "4", "5"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        elif choice == "5":
            result = power(num1, num2)

        print("Result: ", result)

    else:
        print("Invalid choice. Try again.")
