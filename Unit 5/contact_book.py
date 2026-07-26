# contact_book.py

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added.")

def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return None

def delete_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print("Contact deleted.")
            return
    print("Contact not found.")

def view_all():
    if contacts == []:
        print("No contacts.")
    else:
        for contact in contacts:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print()

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        name = input("Enter name: ")
        contact = search_contact(name)

        if contact:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name: ")
        delete_contact(name)

    elif choice == "4":
        view_all()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")