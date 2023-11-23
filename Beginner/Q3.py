def calculate_grade():
    total_marks = 0
    for i in range(1, 6):
        if i==1:
            subject = "Physics"
        elif i==2:
            subject = "Chemistry"
        elif i==3:
            subject = "Biology"
        elif i==4:
            subject = "Mathematics"
        elif i==5:
            subject = "Computer"
        subject = input(f"Enter the marks of {subject} for student: ")
        total_marks += int(subject)

    percentage = (total_marks / 500) * 100

    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    elif percentage >= 40:
        grade = 'E'
    else:
        grade = 'F'

    return percentage, grade

percentage, grade = calculate_grade()
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")