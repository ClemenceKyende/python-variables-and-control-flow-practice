# Triangle Type Checker
# Asking for user input
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))

# Validating the triangle inequality theorem
if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Lengths must be positive numbers.")
elif side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
    print("These lengths do not form a triangle.")
else:
    # Determining triangle type
    if side1 == side2 == side3:
        print("The triangle is Equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")