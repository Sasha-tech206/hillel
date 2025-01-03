while True:
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Error: Unknown operator.")
            continue

        print(f"Result: {result}")

        continue_calc = input("Do you want to perform another calculation? (y/yes to continue, any other key to exit): ").strip().lower()
        if continue_calc not in ("y", "yes"):
            print("Calculator exiting. Thank you!")
            break
    except ValueError:
        print("Error: Please enter valid numbers.")