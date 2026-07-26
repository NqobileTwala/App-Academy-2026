print()
print("Student Information System")
print("--------------------------")
print()

name = input("Enter your first name: ")
surname = input("Enter your last name: ")

age = input("Enter your age: ")
age_int = int(age)

favNumber = input("Enter your favourite number: ")
number_float = float(favNumber)
print()

fullname = name + " " + surname
months = age_int * 12
number_float = round(number_float, 2) 

print(f"Welcome Mr/Ms. {fullname.upper().title()}")
print(f"Age of {months} months")
print(f"Your favourite number is: {number_float}")
print("--------------------------")

print(type(name))
print(type(surname))
print(type(months))
print(type(number_float))