from controllers import ContactManager


class Terminal:
    def __init__(self):
        controller = ContactManager()

        while True:
            line = input()

            if line == "":
                exit(0)
            
            commands = line.split(" ")

            if commands[0] == "AC":
                name = commands[1]
                email_address = input()
                phone_number = input()

                if controller.has_contact(name):
                    print("The contact already exists.")
                else:
                    controller.create_contact(name, email_address, phone_number)
                    print("Contact successfully created.")


            elif commands[0] == "ECE":
                name = commands[1]
                email_address = input()

                if not controller.has_contact(name):
                    print("No such contact.")
                elif not controller.is_valid_email_address(email_address):
                    print("Invalid email")
                else:
                    controller.change_email_address(name, email_address)
                    print("Contact successfully updated.")

            elif commands[0] == "ECP":
                name = commands[1]
                phone_number = input()

                if not controller.has_contact(name):
                    print("No such contact.")
                elif not controller.is_valid_phone_number(phone_number):
                    print("Invalid phone number")
                else:
                    controller.change_phone_number(name, phone_number)
                    print("Contact successfully updated.")

            elif commands[0] == "LC":
                if not controller.has_contacts():
                    print("No contacts available.")
                else:
                    contacts = controller.get_contacts()
                    for contact in contacts:
                        print(contact.get_name())

            elif commands[0] == "SC":
                name = commands[1]
                if not controller.has_contact(name):
                    print("No such contact.")
                else:
                    contact = controller.get_contact(name)
                    print(contact.get_name())
                    print(contact.get_email_address())
                    print(contact.get_phone_number())

            elif commands[0] == "DC":
                name = commands[1]
                name = commands[1]
                if not controller.has_contact(name):
                    print("No such contact.")
                else:
                    controller.delete_contact(name)
                    print("Contact deleted.")

            elif commands[0] == "FC":
                name = commands[1]
                if not controller.has_contacts():
                    print("No contacts available.")
                else:
                    contacts = controller.find_contacts(name)
                    if not contacts:
                        print("No results.")
                    else:
                        for contact in contacts:
                            print(contact.get_name())
