from models import Contact
import re

class ContactManager:
    def __init__(self):
        self.contacts = []
    
    def has_contacts(self):
        return len(self.get_contacts()) > 0
    
    def get_contacts(self):
        return self.contacts
    
    def get_contact(self, name):
        for contact in self.get_contacts():
            if contact.get_name() == name:
                return contact
        return None
    
    def has_contact(self, name):
        return self.get_contact(name) is not None

    def create_contact(self, name, email_address, phone_number):
        contact = Contact(name, email_address, phone_number)
        self.contacts.append(contact)
    
    def delete_contact(self, name):
        contact = self.get_contact(name) 
        self.contacts.remove(contact)
 
    def is_valid_email_address(self, email_address):
        return bool(re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email_address))

    def change_email_address(self, name, email_address):
        contact = self.get_contact(name)
        contact.set_email_address(email_address)
    
    def is_valid_phone_number(self, phone_number):
        return bool(re.match(r"(^[0-9]{9}$)", phone_number))
    
    def change_phone_number(self, name, phone_number):
        contact = self.get_contact(name)
        contact.set_phone_number(phone_number)

    def find_contact(self, name_pattern):
        result = []
        for contact in self.get_contacts():
            if name_pattern in contact.get_name():
                result.append(contact)
        return result
