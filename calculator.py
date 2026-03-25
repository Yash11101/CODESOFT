def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    return "Error: Invalid operation selected."


def main():
    print("Simple Calculator")
    print("Choose an operation: +, -, *, /")

    try:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return

    op = input("Enter operation (+, -, *, /): ").strip()

    result = calculate(number1, number2, op)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
