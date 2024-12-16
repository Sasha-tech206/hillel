num1 = float(input("Please enter your first number: "))
operation = input("Please Enter the mathematical operation: ")
num2 = float(input("Please enter your second number: "))

if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero!")