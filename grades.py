# Define a dictionary to map grade ranges to grade letters
grade_scale = {
    (90, 100): 'A',
    (80, 89): 'B',
    (70, 79): 'C',
    (60, 69): 'D',
    (0, 59): 'F',
}

def calculate_grade(score):
    for (lower, upper), grade in grade_scale.items():
        if lower <= score <= upper:
            return grade

def main():
    num_students = int(input("Enter the number of students: "))
    student_grades = {}

    for i in range(num_students):
        student_name = input(f"Enter the name of student {i + 1}: ")
        student_score = float(input(f"Enter the score for {student_name}: "))
        student_grade = calculate_grade(student_score)
        student_grades[student_name] = (student_score, student_grade)

    print("\nGrades:")
    for student, (score, grade) in student_grades.items():
        print(f"{student}: Score = {score}, Grade = {grade}")

if __name__ == "__main__":
    main()
