def validate_password(password):
    """
    Validate the entered password.

    Args:
    password (str): The password to validate.

    Returns:
    None
    """
    if password == "python123":
        print("Access granted.")
    else:
        print("Access denied.")

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    validate_password(user_password)
