def check_age(age):
    """
    Check the age category of a person.

    Args:
    age (int): The age to check.

    Returns:
    None
    """
    if age < 18:
        print("You are a minor.")
    elif 18 <= age <= 65:
        print("You are an adult.")
    else:
        print("You are a senior.")

if __name__ == "__main__":
    user_age = int(input("Enter your age: "))
    check_age(user_age)
