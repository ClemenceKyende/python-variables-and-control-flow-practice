def day_of_week_checker(day_number):
    """
    Check the day of the week based on the input number.

    Args:
    day_number (int): The number representing the day (1-7).

    Returns:
    None
    """
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if day_number in days:
        print(days[day_number])
    else:
        print("Invalid input.")

if __name__ == "__main__":
    day_num = int(input("Enter a number (1-7): "))
    day_of_week_checker(day_num)
