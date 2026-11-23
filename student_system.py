# STUDENT PERFORMANCE MANAGEMENT SYSTEM

print("STUDENT PERFORMANCE MANAGEMENT SYSTEM")

name = input("Enter student name: ")

student_class = input("Enter student class: ")

subjects = ["Mathematics", "English", "Science",
            "Kiswahili", "Computer"]

marks = {}

for subject in subjects:
    mark = int(input("Enter marks for " + subject + ": "))
    marks[subject] = mark

print("Student information recorded!")
  ##calculations and function 
# FUNCTION 1: Calculate average
def calculate_average(marks):
    total = sum(marks.values())
    average = total / len(marks)
    return total, average


# FUNCTION 2: Get grade
def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "E"


# FUNCTION 3: Get performance
def get_performance(average):
    if average >= 50:
        return "PASS"
    else:
        return "FAIL"


# FUNCTION 4: Display report
def display_report(name, student_class, marks):
    total, average = calculate_average(marks)
    grade = get_grade(average)
    status = get_performance(average)

    best = max(marks, key=marks.get)
    lowest = min(marks, key=marks.get)

    print("\n===== STUDENT REPORT =====")
    print("Student:", name)
    print("Class:", student_class)

    for subject, mark in marks.items():
        print(subject, ":", mark)

    print("Total Marks:", total)
    print("Average:", average)
    print("Grade:", grade)
    print("Status:", status)
    print("Best Subject:", best)
    print("Lowest Subject:", lowest)


# Display the report
display_report(name, student_class, marks)