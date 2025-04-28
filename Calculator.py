def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        
            choice = int(input("\nEnter your choice (1-5): "))

            if choice == 5:
                print("Exiting the calculator. Goodbye!")
                break

            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please choose a valid operation.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                print(f"The result of {num1} + {num2} is {num1 + num2}")
            elif choice == 2:
                print(f"The result of {num1} - {num2} is {num1 - num2}")
            elif choice == 3:
                print(f"The result of {num1} * {num2} is {num1 * num2}")