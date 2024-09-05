from contact_manager import ContactManager
import time


# Initialize Contact Manger 
cm = ContactManager("contacts.csv")

# Handles logic for creating a contact for user abstraction 
def create_contact_handler():
    new_contact = cm.create_contact()
    cm.save_contact_to_csv(new_contact)
    time.sleep(2)
    main()

def read_contact_handler():
    contact_obj_list = cm.read_contact_from_csv()
    cm.print_contacts(contact_obj_list)
    time.sleep(2)
    main()
    
def searach_contact_handler():
    matches = cm.search_contacts()
    if matches is not None:
        cm.print_found_contacts(matches)
    time.sleep(2)
    main()
    
def delete_contact_handler():
    contacts_to_delete = cm.search_contacts()
    indexed_contacts = cm.index_contacts(contacts_to_delete)
    cm.delete_contact(indexed_contacts)
    time.sleep(2)
    main()

def modify_contact_handler():
    contacts_to_modify = cm.search_contacts()
    indexed_contacts = cm.index_contacts(contacts_to_modify)
    cm.modify_contact(indexed_contacts)
    time.sleep(2)
    main()
def main():
    print("\n*** Welcome to my your conatact application ***\n")
    main_menu()

def main_menu():
    print("1: Display Contacts\n2: Create Contact\n3: Update Contact\n4: Search Contact\n5: Delete Contact\nq: Quit")
    option = input("\nSelect an option from the menu below to contune...")
    match option:
        case "1":
            read_contact_handler()
        case "2":
            create_contact_handler()
        case "3":
            modify_contact_handler()
        case "4":
            searach_contact_handler()
        case "5":
            delete_contact_handler()
        case "q":
            quit()
        case _:
            raise ValueError("Incorrect input entered!!!")
            
            

if __name__ == "__main__":
    main()