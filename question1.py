def arithmetic_operations(a, b):
    """
    Performs basic arithmetic operations on two numbers and prints the results.
    """
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Undefined (division by zero)"

    print(f"The result of adding {a} and {b} is: {addition}")
    print(f"The result of subtracting {b} from {a} is: {subtraction}")
    print(f"The result of multiplying {a} by {b} is: {multiplication}")
    print(f"The result of dividing {a} by {b} is: {division}")

# Example usage
arithmetic_operations(10, 5)
