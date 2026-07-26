print()
print("Multi-Function Calculator")
print("-------------------------")
print()

num1 = float(input("Enter your desired first number: "))
num2 = float(input("Enter an alternative number: "))
print()

# num1 = int(num1)
# num2 = int(num2)



print(round (num1 + num2, 2))
print(round(num1 - num2, 2))
print(round(num1 * num2, 2))


if num2 == 0:
    print("Error")
else:
    round(num1 / num2, 2)
    round(num1 // num2, 2)
    round(num1 % num2, 2)



print(f"")

