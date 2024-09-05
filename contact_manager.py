from contact import Contact
import csv
import re


class ContactManager:
    
    def __init__(self, contact_csv):
        self.contacts = contact_csv
        self.contact_objs = []
    
    @staticmethod
    def create_contact():
        try:
            first_name = (input("Enter First Name\n")).capitalize()
            assert first_name is not None
            last_name = (input("Enter Last Name\n")).capitalize()
            assert last_name is not None
            phone = input("Enter Phone Number \n")
            assert phone is not None
            email = input("Enter Email Address\n")
            assert email is not None
            
            # Email Regex for email validation 
            email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            
            if not re.match(email_regex, email):
                raise ValueError("\nEmail is incorrectly formatted\n")
                
            return Contact(first_name, last_name, phone, email)
        
        except AssertionError:
            print("No data has been entered for one or more fields")
            
    
    def save_contact_to_csv(self,contact):
        try:
            with open(self.contacts, 'a') as f:
                writer = csv.writer(f)
                writer.writerow([contact.first_name,contact.last_name,contact.phone,contact.email])
        except Exception as e:
            print("Error saving contact to file\n", e)
        else:
            print("\nContact created succesfully\n")
            print("-------------------------\n")
            print(f'New Contact:\n{contact}\n')
            print("-------------------------")
            
            
    def save_contacts_to_csv(self, contacts):
        try:
            with open(self.contacts, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(["First Name","Last Name","Phone Number","Email Address"])
                for contact in contacts:
                    writer.writerow([contact.first_name,contact.last_name,contact.phone,contact.email])
        except Exception as e:
            print("Error saving contact to file\n", e)
        
        
    def read_contact_from_csv(self):
        try:
            
            with open(self.contacts, "r") as f:
                next(f) #Header 
                contact_csv = csv.reader(f)
                for row in contact_csv:
                    new_contact = Contact(row[0], row[1], row[2], row[3])
                    self.contact_objs.append(new_contact)
        except Exception as e:
            print("Error reading contacts from csv", e)
            print(self.contact_objs)
        else:
            return self.contact_objs
    
    
    # Reinitialize list of contact objects
    def reset_contacts(self):
        self.contact_objs = []
            
            
    def print_contacts(self, contact_list):
        index = 1
        print("\n***Contact List***\n")
        print("-------------------------")
        for contact in contact_list:
            print(f'{index}: {repr(contact)}')
            index +=1
            
        print("\n-------------------------\n")
        self.reset_contacts()
        
        
    def search_contacts(self):
        try:
            contact_matches = []
            contact_flg = False
            name_of_contact = input("\nEnter the name of the contact you are searching for...").lower().capitalize()
            self.read_contact_from_csv()
            # Checks if contact is found, updates contact flag and adds it to cotnact_matches array
            for contact in self.contact_objs:
                if contact.first_name == name_of_contact:
                    contact_flg = True
                    contact_matches.append(contact)
                    
            if not contact_flg:
                print(f'\nNo Contact(s) matching the name {name_of_contact} found!')
                self.reset_contacts()
                return
            
            return contact_matches
                  
        except Exception as e:
            print("Error while searching for contact", e)
                
    
    def print_found_contacts(self, found_contacts):
        print("-------------------------")
        print(f'\nContact(s) Found:')
        # Reads contact Matches from contact_matches array and prints them 
        for contact in found_contacts:
            print(contact)
        print("\n-------------------------\n")
        self.reset_contacts()
   
   
    def index_contacts(self, contacts):
        index = 1
        # Dictionary to store search matches in case of duplicates. Allows user to select using an index. 
        contacts_as_dictionary = {}
        
        if contacts is None:
            self.reset_contacts()
            return
        
        for contact in contacts:
            print(f'\n{index}: {repr(contact)}')
            contacts_as_dictionary.update({index: contact})
            index += 1
            
        return contacts_as_dictionary
        
         
    def delete_contact(self, contacts_to_delete):
    
        try:
            if contacts_to_delete is None:
                return
            delete_option = int(input("\nEnter index of contact to delete..."))
            if delete_option not in contacts_to_delete.keys():
                print("\nInvalid index selected\n")
                return
            
            # Contact to delete 
            contact_to_delete = contacts_to_delete[delete_option]
            
            # Removed contact from list of contact objects
            self.contact_objs.remove(contact_to_delete)

            # Overwriting contacts.csv with list of contact objects minus the deleted contact
            with open(self.contacts, "w") as f:
                writer = csv.writer(f)
                writer.writerow(["First Name","Last Name","Phone Number","Email Address"])
                
                for contact in self.contact_objs:
                    writer.writerow([contact.first_name,contact.last_name,contact.phone, contact.email])
            
            print(f'\nContact Deleted Succesfully:\n{contact_to_delete}\n')
                
        except Exception as e:
            print("\nError occoured deleteing contact\n", e)
        
        finally:
            self.reset_contacts()
        
    
    def modify_contact(self, contacts_to_modify):
        
        try:
            if contacts_to_modify is None:
                return
            
            modify_option = int(input("\nEnter index of contact to modify..."))
            if modify_option not in contacts_to_modify.keys():
                print("\nInvalid index selected\n")
                return
            
            contact_to_modify = contacts_to_modify[modify_option]
            print(f"Modifying Contact\n{contact_to_modify}\n")
            modified_contact = self.create_contact()
            self.contact_objs = [modified_contact if contact == contact_to_modify else contact for contact in self.contact_objs]
            self.save_contacts_to_csv(self.contact_objs)
            
        except Exception as e:
            print("Error modifying contatact\n", e)
            
        else:
            print("\nContact Modified Succesfully")
            print(modified_contact)
        finally:
            self.reset_contacts()
        