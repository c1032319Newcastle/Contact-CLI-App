# Contact Management Application

This Contact Management App allows users to create, read, update, delete, and search for contacts within a CSV file. It is designed to handle contact information such as first name, last name, phone number, and email address.

## Features

- **Create Contacts**: Add new contacts to the CSV file.
- **View Contacts**: Display all stored contacts.
- **Search Contacts**: Search for specific contacts by name.
- **Delete Contacts**: Remove a contact from the CSV file.
- **Update Contacts**: Modify an existing contact's details.

## File Structure

- `contact_manager.py`: Handles the contact-related operations such as creating, reading, updating, deleting, and searching for contacts.
- `main.py`: Contains the main logic for interacting with the user and calling the respective operations.
- `contacts.csv`: A CSV file that stores all the contact information.

## How to Use

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    ```

2. **Install dependencies**:
    No external dependencies are required for this project, as it uses Python’s built-in libraries like `csv` and `re`.

3. **Run the application**:
    ```bash
    python main.py
    ```

4. **Main Menu**:
    Once the program is running, you'll be presented with the following menu options:

    ```
    *** Welcome to your contact application ***
    1: Display Contacts
    2: Create Contact
    3: Update Contact
    4: Search Contact
    5: Delete Contact
    q: Quit
    ```

### Menu Options

1. **Display Contacts**: Lists all the contacts saved in the `contacts.csv` file.
2. **Create Contact**: Allows the user to add a new contact. Prompts for first name, last name, phone number, and email address. The email is validated with a regular expression.
3. **Update Contact**: Search for a contact, then choose the contact to modify. This feature has not been implemented fully yet.
4. **Search Contact**: Search for a contact by first name. If there are matches, they are displayed to the user.
5. **Delete Contact**: Search for a contact to delete, choose the correct one based on an index, and then delete it from the CSV file.
6. **Quit**: Exits the application.

## Code Overview

### `contact_manager.py`

This file contains the `ContactManager` class, which handles all the contact operations:

- **`create_contact`**: Collects user input for contact details and validates the email address format.
- **`save_contact_to_csv`**: Saves a contact to the `contacts.csv` file.
- **`read_contact_from_csv`**: Reads all contacts from the CSV file and stores them as `Contact` objects.
- **`search_contacts`**: Finds contacts by first name.
- **`delete_contact`**: Deletes a selected contact from the CSV file.
- **`modify_contact`**: (Not fully implemented) Will allow updating existing contact details.

### `main.py`

This file contains the main logic for the program. It provides a simple text-based user interface and interacts with the `ContactManager` class for performing the operations. Key functions:

- **`create_contact_handler`**: Collects new contact data from the user and saves it.
- **`read_contact_handler`**: Displays the list of all saved contacts.
- **`searach_contact_handler`**: Searches for a contact by name.
- **`delete_contact_handler`**: Searches for and deletes a contact.
- **`modify_contact_handler`**: Searches for and modifies a contact (currently not implemented).
- **`main_menu`**: Displays the main menu options and routes the user to the selected operation.

### CSV File: `contacts.csv`

The CSV file format is as follows:

| First Name  | Last Name  | Phone Number | Email Address        |
|-------------|------------|--------------|----------------------|
| John        | Doe        | 123-456-7890 | john.doe@example.com |

The first row of the CSV file is a header, and the subsequent rows represent individual contacts.


