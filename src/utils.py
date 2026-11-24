def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ")

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        else:
            raise ValueError("Invalid operator")

        print("Result:", result)

    except ValueError as e:
        print("Input error:", e)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except Exception as e:
        print("Unexpected error:", e)

calculator()