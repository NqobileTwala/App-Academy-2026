# The Phone Directory Search

print("The Phone Directory Search")
print("--------------------------")
print("")

contacts = {
    "Liam": "0875471643",
    "Matt": "0664292647",
    "Lucky": "0217463996"
}

friend = input("Enter the name of the friend you're looking for: ").title().strip()

# print(contacts[friend])

if friend in contacts:
    print(f"Found! {friend}'s number is {contacts[friend]}")
else:
    print("Contact not found.")
