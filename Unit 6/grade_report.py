# Grade report generator

students = [
    {"name": "John", "maths": 80, "english": 75, "science": 90},
    {"name": "Mary", "maths": 65, "english": 70, "science": 60},
    {"name": "Peter", "maths": 50, "english": 55, "science": 45},
    {"name": "Sarah", "maths": 85, "english": 90, "science": 95},
    {"name": "James", "maths": 30, "english": 40, "science": 35}
]

results = []

total = 0
highest = 0
lowest = 100

for student in students:

    average = (student["maths"] + student["english"] + student["science"]) / 3

    if average >= 80 and average <= 100:
        grade = "A"
        status = "Pass"

    elif average >= 70 and average <= 79:
        grade = "B"
        status = "Pass"

    elif average >= 60 and average <= 69:
        grade = "C"
        status = "Pass"

    elif average >= 50 and average <= 59:
        grade = "D"
        status = "Pass"

    elif average >= 40 and average <= 49:
        grade = "F"
        status = "Fail"

    elif average > 100 or average < 0:
        grade = "Invalid"
        status = "Invalid"

    else:
        grade = "Needs Intervention"
        status = "Fail"

    result = {
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    }

    results.append(result)

    total = total + average

    if average > highest:
        highest = average

    if average < lowest:
        lowest = average

class_average = total / len(students)

print("CLASS REPORT")
print()

for result in results:
    print("Name:", result["name"])
    print("Average:", round(result["average"], 2))
    print("Grade:", result["grade"])
    print("Status:", result["status"])
    print()

print("Class Average:", round(class_average, 2))
print("Highest Average:", round(highest, 2))
print("Lowest Average:", round(lowest, 2))

while True:
    name = input("Enter student name to search (or 'exit'): ")

    if name == "exit":
        break

    found = False

    for result in results:
        if result["name"] == name:
            print("Name:", result["name"])
            print("Average:", round(result["average"], 2))
            print("Grade:", result["grade"])
            print("Status:", result["status"])
            found = True

    if found == False:
        print("Student not found.")