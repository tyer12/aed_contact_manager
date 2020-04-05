![Tests](https://github.com/amgs/aed_contact_manager/workflows/Tests/badge.svg)

# Contact Manager

This application is a case study for the development of a GUI with Python 3.

The example is a contact management application. It implements a few basic operations on the command line, which are also offered by the GUI.

## Command line operations

### **AC**: Add Contact
Registers a new contact with the given information.

- Usage:

        AC Name
        EmailAddress
        PhoneNumber

- Output:
  - Success:
        
        Contact successfully created.

  - Failure:
  
        The contact already exists.

### **ECE**: Edit Contact Email
Changes the email address of a contact.

- Usage:

        ECE Name
        NewEmailAddress

- Output:
  - Success:
  
        Contact successfully updated.
        
  - Failure:
        
        There is no such contact.
        Invalid email.
        
### **ECP**: Edit Contact Phone
Changes the phone number of a contact.

- Usage:
  
        ECP Name
        NewPhoneNumber

- Output:
  - Success:
        
        The contact was successfully updated.

  - Failure:

        There is no such contact.
        Invalid phone number.
    
### **LC**: List Contacts
Lists all contacts, showing the names.

- Usage: 
    
        LC

- Output:
  - Success:
  
        Name
        Name
        ...

  - Failure:
        
        No contacts available.

### **SC**: Show contact
Shows all the information about a contact.

- Usage:
        SC Name

- Output:
  - Success:

        Name
        EmailAddress
        PhoneNumber

  - Failure:
        
        No such contact.
        
### **DC**: Delete Contact
Deletes the contact with the given name.

- Usage: 

        DC Name

- Output:
  - Success:
        
        Contact deleted.

  - Failure:

        No such contact.

### **FC**: Find Contact
List contacts whose names match the given pattern.

- Usage: 
    
    SC PartialName

- Output:
  - Success with results:
      
        Name
        Name
        ...
  
  - Success without results:
  
        No results.
  
  - Failure:

        No contacts available.