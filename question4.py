def simple_calculator(num1, num2, operation):
    """
    Perform basic arithmetic operations based on user input.

    Args:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform (+, -, *, /).

    Returns:
    None
    """
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Undefined (division by zero)"
    else:
        result = "Invalid operation"

    print(f"Result: {result}")

if __name__ == "__main__":
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")
    simple_calculator(first_num, second_num, op)
