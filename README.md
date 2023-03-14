<h1 align="center"> Bank Management System 🏦 </h1>

## About
The Bank Management System is a software application designed to handle various banking activities such as account creation, deposit, withdrawal, money transfer, account balance inquiry, and transaction history. It provides a user-friendly interface to customers and bank employees to manage their banking operations efficiently.



## Features
* User login and Create Account
* Deposit and withdrawal transactions
* Account balance inquiry
* Transaction history view


## Requirements
* Python 3.x
* Tkinter library (which is usually included with Python)


## Getting Started
1. Clone this repository to your local machine.
2. Open a terminal window and navigate to the cloned repository.
3. Run the following command to start the program: python bank-management.py

## Code Structure

The code is organized into the following functions:

- `__init__(self, master)` : This function initializes the BankSystem object with the specified parameters, sets the title and geometry of the main window, and creates the "Create Account" and "Login" frames.
- `create_account()` : This function creates a new account with the name, age, salary, and PIN entered by the user in the corresponding Entry widgets. It adds the account details to a dictionary and saves the dictionary to a file using the `pickle` module.
- `login()` : This function validates the entered PIN against the saved account details and displays the account information if the PIN is correct.
- `load_accounts()` : This function loads the saved account details from the file using the `pickle` module and returns the dictionary.

### The code also defines the following labels and buttons for the game:

- Labels:
    - `name_label` : This label displays "Name:" in the "Create Account" frame.
    - `age_label` : This label displays "Age:" in the "Create Account" frame.
    - `salary_label` : This label displays "Salary:" in the "Create Account" frame.
    - `pin_label` : This label displays "PIN:" in the "Create Account" frame.
    - `login_pin_label` : This label displays "PIN:" in the "Login" frame.
- Entry widgets:
    - `name_entry` : This Entry widget allows the user to enter their name in the "Create Account" frame.
    - `age_entry` : This Entry widget allows the user to enter their age in the "Create Account" frame.
    - `salary_entry` : This Entry widget allows the user to enter their salary in the "Create Account" frame.
    - `pin_entry` : This Entry widget allows the user to enter their PIN in the "Create Account" frame.
    - `login_pin_entry` : This Entry widget allows the user to enter their PIN in the "Login" frame.
- Buttons:
    - `create_account_button` : This button calls the `create_account()` function when clicked.
    - `login_button` : This button calls the `login()` function when clicked.



<div align="center">
  
## Made with ❤️ , Python, and Tkinter. Enjoy!
  
</div>

