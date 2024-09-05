class Contact:

    # Initialization of Contact Object 
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        
   # Getter and Setter Methods for accessing Contact obbject attributes
    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self, new_name):
        self.first_name = new_name
        
    def get_last_name(self):
        return self.last_name
    
    def set_last_name(self, new_name):
        self.last_name = new_name
    
    def get_phone(self):
        return self.phone
    
    def set_phone(self, new_number):
        self.phone = new_number
    
    def get_email(self):
        return self.email
    
    def set_email(self, new_email):
        self.email = new_email
        
    # String representation of Contact object
    def __str__(self):
        return f'\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nPhone Number: {self.phone}\nEmail Address: {self.email}'
    
    def __repr__(self):
        return f'Contact({self.first_name}, {self.last_name}, {self.phone}, {self.email})'