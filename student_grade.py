def calculate_average(marks):
    return sum(marks) / len(marks)

def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def validate_marks(marks):
    for mark in marks:
        if mark < 0 or mark > 100:
            return False
    return True

student_name = input("Enter student name: ")
marks_input = input("Enter marks separated by space: ")

marks = list(map(int, marks_input.split()))


if validate_marks(marks):
    average = calculate_average(marks)
    grade = get_grade(average)

    print(f"\nStudent: {student_name}")
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
else:
    print("Error: One or more marks are invalid (must be between 0 and 100).")
