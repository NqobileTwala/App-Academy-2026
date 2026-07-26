# Adding 2 numbers

# num1 = input("Enter the first number: ")
# num2 = input("Enter second number: ")

# # print(num1 + num2)

# # Type Casting: moving from one data type to another
# print(int(num1) + int(num2))

# CORE DATA TYPES:

## str: Strings/Text
## Int: Integer/Whole numbers
## float: Decimals
## bool: True/False

# Calculating Bill Tip

bill = float(input("Enter total for the bill: R"))
tip = 0.15 # 15% written in decimal

value_tip = bill * tip

total_cost = bill + value_tip

round(print(f"Here is the tip: {value_tip}"))
print(f"This is the total bill: {total_cost}")