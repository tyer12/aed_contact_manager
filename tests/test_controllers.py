import unittest
from controllers import ContactManager
from models import Contact

class TestContactManager(unittest.TestCase):
    def setUp(self):
        self.cm = ContactManager()
        self.contact = Contact("Bob", "email@example.com", "123456789")
    
    def add_contact(self):
        self.cm.contacts.append(self.contact)
    
    def test_has_contacts(self):
        self.assertTrue(self.cm.has_contacts())
        self.add_contact()
        self.assertTrue(self.cm.has_contacts())
    
    def test_get_contacts(self):
        self.assertEqual(self.cm.get_contacts(), [])
        self.add_contact()
        self.assertEqual(self.cm.get_contacts(), [self.contact])

    def test_get_contact(self):
        self.assertIsNone(self.cm.get_contact(self.contact.get_name()))
        self.add_contact()
        self.assertEqual(self.cm.get_contact(self.contact.get_name()), self.contact)

    def test_has_contact(self):
        self.assertFalse(self.cm.has_contact(self.contact.get_name()))
        self.add_contact()
        self.assertTrue(self.cm.has_contact(self.contact.get_name()))
    
    def test_create_contact(self):
        self.cm.create_contact(self.contact.get_name(),  
            self.contact.get_email_address(), 
            self.contact.get_phone_number())
        self.assertEqual(self.cm.get_contacts()[0].get_name(), self.contact.get_name())
        self.assertEqual(self.cm.get_contacts()[0].get_email_address(), self.contact.get_email_address())
        self.assertEqual(self.cm.get_contacts()[0].get_phone_number(), self.contact.get_phone_number())

    def test_delete_contact(self):
        self.add_contact()
        self.cm.delete_contact(self.contact.get_name())
        self.assertListEqual(self.cm.get_contacts(), [])
    
    def test_change_email_address(self):
        self.add_contact()
        self.assertEqual(self.cm.get_contact(self.contact.get_name()).get_email_address(), self.contact.get_email_address())
        self.cm.change_email_address(self.contact.get_name(), "NEWEMAIL@example.com")
        self.assertEqual(self.cm.get_contact(self.contact.get_name()).get_email_address(), "NEWEMAIL@example.com")

    def test_is_valid_email_address(self):
        self.assertTrue(self.cm.is_valid_email_address("a@a.a"))
        self.assertFalse(self.cm.is_valid_email_address("a@a"))
        self.assertFalse(self.cm.is_valid_email_address(""))

    def test_change_phone_number(self):
        self.add_contact()
        self.assertEqual(self.cm.get_contact(self.contact.get_name()).get_phone_number(), self.contact.get_phone_number())
        self.cm.change_phone_number(self.contact.get_name(), "987654321")
        self.assertEqual(self.cm.get_contact(self.contact.get_name()).get_phone_number(), "987654321")


    def test_is_valid_phone_number(self):
        self.assertTrue(self.cm.is_valid_phone_number("999999999"))
        self.assertFalse(self.cm.is_valid_phone_number("99999999"))
        self.assertFalse(self.cm.is_valid_phone_number(""))
        self.assertFalse(self.cm.is_valid_phone_number("9999999999"))

    def test_find_contacts(self):
        self.add_contact()
        contacts = self.cm.find_contacts("alice")
        self.assertListEqual(contacts, [])
        contacts = self.cm.find_contacts("o")
        self.assertListEqual(contacts, [self.contact])
        contacts = self.cm.find_contacts("")
        self.assertListEqual(contacts, [self.contact])

if __name__ == "__main__":
    unittest.main()
    