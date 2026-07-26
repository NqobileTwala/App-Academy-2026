print()

print("Username and Message Formatter")
print("------------------------------")
print()

name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
bio = input("Enter a short bio message: ").strip()
print()

username = f"{name[0]}{last_name}".lower()

full_name = name + " " + last_name
full_name = full_name.title()

num_of_char = len(bio)
new_bio = bio.replace("I am", "I'm")

# print(username)
# print(full_name)
# print(num_of_char)
# print(new)

print(f"My name is {full_name}, but you can call me {username} for short, I guess. {new_bio}")

