print()

print("The secure Password Hint Tool")
print("-----------------------------")

password = input("Please enter your password: ").strip()

# pass_hint = password[0] + password[-1]


print(f"Your password hint: It starts with \"{password[0].upper()}\" and ends with \"{password[-1].upper()}\".")

