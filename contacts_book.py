contacts = {}

def add_contact():
    name = input("enter contact name:")
    phone = input("enter phone number:")
    email = input("enter email:")
    address = input("enter address:")

    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("no contacts found.\n")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"phone: {info['phone']}")
            print(f"email: {info['email']}")
            print(f"address: {info['address']}")
            print("--------------------")

def search_contact():
    name = input("enter contact name to search:")
    if name in contacts:
        print("contact found:")
        print(contacts[name])
    else:
        print("contact not found.\n")

def update_contact():
    name = input("enter contact name to update:")
    if name in contacts:
        phone = input("enter new phone:")
        email = input("enter new email:")
        address = input("enter new address:")

        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("contact updated successfully!")
    else:
        print("contact not found.\n")
def delete_contact():
    name = input("enter name to delete:")
    if name in contacts:
        del contacts[name]
        print("contact deleted successfully!\n")
    else:
        print("contact not found.\n")

while True:
    print("contact book menu")
    print("1.add contact")
    print("2.view contacts")
    print("3.search contact")
    print("4.update contact")
    print("5.delete contact")
    print("6.exit")

    choice = input("enter your choice:")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("exiting contact book.")
        break
    else:
        print("invalid choice. try again.\n")
