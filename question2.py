def odd_or_even_checker():
    """
    Checks whether a number entered by the user is odd or even.
    """
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"The number {number} is Even.")
    else:
        print(f"The number {number} is Odd.")

# Example usage
odd_or_even_checker()
