# Password Validator
# Asking for user input
password = input("Enter your password: ")

# Checking password
if password == "python123":
    print("Access granted.")
else:
    print("Access denied.")
    # Provide hints for creating a stronger password
    print("Tips for a stronger password:")
    print("- Use at least 8 characters.")
    print("- Include both uppercase and lowercase letters.")
    print("- Use numbers and symbols.")