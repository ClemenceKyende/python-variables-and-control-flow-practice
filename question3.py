def grade_categorizer():
    """
    Categorizes the user's score into grades.
    """
    score = int(input("Enter your score (0-100): "))
    if 90 <= score <= 100:
        print(f"With a score of {score}, you earned a Grade: A")
    elif 80 <= score < 90:
        print(f"With a score of {score}, you earned a Grade: B")
    elif 70 <= score < 80:
        print(f"With a score of {score}, you earned a Grade: C")
    elif 60 <= score < 70:
        print(f"With a score of {score}, you earned a Grade: D")
    elif 0 <= score < 60:
        print(f"With a score of {score}, you earned a Grade: F")
    else:
        print(f"{score} is an invalid score. Please enter a score between 0 and 100.")

# Example usage
grade_categorizer()
