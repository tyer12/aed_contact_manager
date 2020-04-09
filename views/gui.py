from controllers import ContactManager
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

class ContactManagerGUI:
    def __init__(self):
        self.cm = ContactManager()
        self.run()
    
    def run(self):
        self.window = Tk()
        self.window.title("Contact Manager")
        self.window.geometry('450x185')

        frm_content = Frame(self.window)
        frm_content.grid(column=0, row=0)
        self.listbox = Listbox(frm_content, width=40, height=10)
        self.listbox.grid(column=0, row=0)
        self.listbox.bind('<<ListboxSelect>>', self.show_detail)

        frm_detail= Frame(frm_content)
        frm_detail.grid(sticky=N, column=1, row=0)
        detail_title = Label(frm_detail, text="Details:", justify=LEFT)
        detail_title.pack(side=TOP)
        self.detail_name = Label(frm_detail, text="-", justify=LEFT)
        self.detail_name.pack(side=TOP)
        self.detail_email_address = Label(frm_detail, text="-", justify=LEFT)
        self.detail_email_address.pack(side=TOP)
        self.detail_phone_number = Label(frm_detail, text="-", justify=LEFT)
        self.detail_phone_number.pack(side=TOP)
        
        frm_buttons = Frame(self.window)
        frm_buttons.grid(sticky=W, column=0, row=1)
        btn_add_contact = Button(frm_buttons, text="Add contact", command=self.btn_add_contact_action)
        btn_add_contact.pack(side=LEFT)
        btn_remove_contact = Button(frm_buttons, text="Remove contact", command=self.btn_remove_contact_action)
        btn_remove_contact.pack(side=LEFT)

        frm_find = Frame(frm_buttons)
        frm_find.pack(side=RIGHT)
        self.ent_find_contacts = Entry(frm_find)
        btn_find_contacts = Button(frm_find, text="Find contacts", command= lambda: self.btn_find_contacts_action(self.ent_find_contacts.get()))
        btn_find_contacts_cancel = Button(frm_find, text="x", command=self.btn_find_contacts_cancel_action)
        btn_find_contacts.pack(side=LEFT)
        btn_find_contacts_cancel.pack(side=RIGHT)
        self.ent_find_contacts.pack(side=RIGHT)

        frm_status = Frame(self.window)
        frm_status.grid(sticky=W, column=0, row=2)
        self.status = Label(frm_status, text="OK", justify=LEFT)
        self.status.grid(sticky=W, column=0, row=0)
        
        self.populate_list()
        self.window.mainloop()
    
    def populate_list(self, contacts=None):
        self.listbox.delete(0, END)
        self.detail_name.config(text="-")
        self.detail_email_address.config(text="-")
        self.detail_phone_number.config(text="-")
        if contacts is None:
            contact_list = self.cm.get_contacts()
        else:
            contact_list = contacts
        for contact in contact_list:
            self.listbox.insert(END, contact.get_name())
    
    def show_detail(self, idx):
        selected_name = self.listbox.get(ACTIVE)
        contact = self.cm.get_contact(selected_name)
        if contact is not None:
            self.detail_name.config(text=contact.get_name(), justify=LEFT)
            self.detail_email_address.config(text=contact.get_email_address(), justify=LEFT)
            self.detail_phone_number.config(text=contact.get_phone_number(), justify=LEFT)
    
    def btn_add_contact_action(self):
        wnd_add_contact = Toplevel(self.window)
        wnd_add_contact.title("Add contact")
        wnd_add_contact.geometry('235x82')
        Label(wnd_add_contact, text="Name", justify=LEFT).grid(sticky=W, column=0, row=0)
        Label(wnd_add_contact, text="Email address", justify=LEFT).grid(sticky=W, column=0, row=1)
        Label(wnd_add_contact, text="Phone number", justify=LEFT).grid(sticky=W, column=0, row=2)
        self.add_contact_name = Entry(wnd_add_contact, width=21)
        self.add_contact_name.grid(column=1, row=0)
        self.add_contact_email_address = Entry(wnd_add_contact, width=21)
        self.add_contact_email_address.grid(column=1, row=1)
        self.add_contact_phone_number = Entry(wnd_add_contact, width=21)
        self.add_contact_phone_number.grid(column=1, row=2)
        Button(wnd_add_contact, text="Add", command= lambda: self.btn_add_contact_add_action(wnd_add_contact)).grid(sticky=W, column=0, row=3)
        Button(wnd_add_contact, text="Cancel", command=wnd_add_contact.destroy).grid(sticky=E, column=1, row=3)

    def btn_add_contact_add_action(self, parent):
        name = self.add_contact_name.get()
        email_address = self.add_contact_email_address.get()
        phone_number = self.add_contact_phone_number.get()
        if self.cm.is_valid_email_address(email_address) == True:
            if self.cm.is_valid_phone_number(phone_number) == True:
                self.cm.create_contact(name, email_address, phone_number)
                self.populate_list()
                parent.destroy()
            else:
                messagebox.showwarning("Invalid", "Invalid phone number!")
                parent.deiconify()
        else:
            messagebox.showwarning("Invalid", "Invalid email!")
            parent.deiconify()

    def btn_remove_contact_action(self):
        selected_name = self.listbox.get(ACTIVE)
        contact = self.cm.get_contact(selected_name)
        if contact is not None:
            self.cm.delete_contact(contact.get_name())
            self.populate_list()

    def btn_find_contacts_action(self, name):
        contacts = self.cm.find_contacts(name)
        if contacts:
            self.status.config(text="Found contacts!", justify=LEFT)
            self.populate_list(contacts)
        else:
            self.status.config(text="No contacts found.", justify=LEFT)

    def btn_find_contacts_cancel_action(self):
        self.status.config(text="OK", justify=LEFT)
        self.ent_find_contacts.delete(0, END)
        self.populate_list()
