# Basic IF/ELSE statement script

age = int(input("Enter your age: "))

section_pass = input("Do you have a VIP ticket? (Yes/No): ").lower()

if age >= 18 and section_pass == "yes":
    print("You have access to the VIP section")
elif age >= 18: 
    print("Access Granted to general section")
else:
    print("Access Denied!")