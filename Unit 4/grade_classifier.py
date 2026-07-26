print()
print("Student Grade Classifier")
print("------------------------")

#name = input("Enter your name: ")
mark1 = float(input("Enter the mark for your first subject: "))
mark2 = float(input("Enter the mark for your second subject: "))
mark3 = float(input("Enter the mark for your thirth subject: "))
print()

average_mark = (mark1 + mark2 + mark3) / 3
average_mark = round(average_mark)
print(f"Total student Average: {average_mark}")

# marks = mark1 and mark2 and mark3

if average_mark >= 80 and average_mark <= 100:
    print("Grade: A")
elif average_mark >= 70 and average_mark <= 79:
    print("Grade: B")
elif average_mark >= 60 and average_mark <= 69:
    print("Grade: C")
elif average_mark >= 50 and average_mark <= 59:
    print("Grade: D")
elif average_mark >= 40 and average_mark <= 49:
    print("Grade: F")
elif average_mark > 100 or average_mark < 0:
    print("INVALID MARK!")
else:
    print("NEEDS INTERVENTION!")


if average_mark >= 50:
    print("Status: PASS")
else:
    print("Status: FAIL")