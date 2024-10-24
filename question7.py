def triangle_type_checker(side1, side2, side3):
    """
    Determine the type of triangle based on the lengths of its sides.

    Args:
    side1 (float): Length of side 1.
    side2 (float): Length of side 2.
    side3 (float): Length of side 3.

    Returns:
    None
    """
    if side1 == side2 == side3:
        print("Equilateral")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Isosceles")
    else:
        print("Scalene")

if __name__ == "__main__":
    s1 = float(input("Enter length of side 1: "))
    s2 = float(input("Enter length of side 2: "))
    s3 = float(input("Enter length of side 3: "))
    triangle_type_checker(s1, s2, s3)
