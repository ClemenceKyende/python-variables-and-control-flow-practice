# Simple Age Checker
# Asking for user input
age = int(input("Enter your age: "))

# Checking age category
if age < 18:
    print(f"At {age} years old, you are a minor.")
elif 18 <= age <= 65:
    print(f"At {age} years old, you are an adult.")
else:
    print(f"At {age} years old, you are a senior.")