class Contact:
    def __init__(self, name, email_address, phone_number):
        self.name = name
        self.email_address = email_address
        self.phone_number = phone_number
    
    def get_name(self):
        return self.name
    
    def get_email_address(self):
        return self.email_address
    
    def set_email_address(self, email_address):
        self.email_address = email_address
    
    def get_phone_number(self):
        return self.phone_number
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number