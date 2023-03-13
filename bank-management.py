from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

class BankSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Bank Management System")
        self.master.geometry("400x300")
        
        # Create Account Frame
        self.create_account_frame = Frame(self.master)
        self.create_account_frame.pack()
        self.name_label = Label(self.create_account_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = Entry(self.create_account_frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.age_label = Label(self.create_account_frame, text="Age:")
        self.age_label.grid(row=1, column=0, padx=10, pady=10)
        self.age_entry = Entry(self.create_account_frame)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)
        self.salary_label = Label(self.create_account_frame, text="Salary:")
        self.salary_label.grid(row=2, column=0, padx=10, pady=10)
        self.salary_entry = Entry(self.create_account_frame)
        self.salary_entry.grid(row=2, column=1, padx=10, pady=10)
        self.pin_label = Label(self.create_account_frame, text="PIN:")
        self.pin_label.grid(row=3, column=0, padx=10, pady=10)
        self.pin_entry = Entry(self.create_account_frame, show="*")
        self.pin_entry.grid(row=3, column=1, padx=10, pady=10)
        self.create_account_button = Button(self.create_account_frame, text="Create Account", command=self.create_account)
        self.create_account_button.grid(row=4, column=1, padx=10, pady=10)
        
        # Login Frame
        self.login_frame = Frame(self.master)
        self.login_frame.pack()
        self.login_pin_label = Label(self.login_frame, text="PIN:")
        self.login_pin_label.grid(row=0, column=0, padx=10, pady=10)
        self.login_pin_entry = Entry(self.login_frame, show="*")
        self.login_pin_entry.grid(row=0, column=1, padx=10, pady=10)
        self.login_button = Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=1, column=1, padx=10, pady=10)
        self.master.bind('<Return>', self.login) # Allow login with "Enter" key
        
        # User Details Frame
        self.user_details_frame = Frame(self.master)
        self.name_label2 = Label(self.user_details_frame, text="Name:")
        self.name_label2.grid(row=0, column=0, padx=10, pady=10)
        self.age_label2 = Label(self.user_details_frame, text="Age:")
        self.age_label2.grid(row=1, column=0, padx=10, pady=10)
        self.salary_label2 = Label(self.user_details_frame, text="Salary:")
        self.salary_label2.grid(row=2, column=0, padx=10, pady=10)
        self.current_balance_label = Label(self.user_details_frame, text="Current Balance:")
        self.current_balance_label.grid(row=3, column=0, padx=10, pady=10)
        self.view_transaction_button = Button(self.user_details_frame, text="View Transaction Log", command=self.view_transaction_log)
        self.view_transaction_button.grid(row=4,column=1, padx=10, pady=10)
        self.deposit_button = Button(self.user_details_frame, text="Deposit", command=self.deposit)
        self.deposit_button.grid(row=5, column=0, padx=10, pady=10)
        self.withdraw_button = Button(self.user_details_frame, text="Withdraw", command=self.withdraw)
        self.withdraw_button.grid(row=5, column=1, padx=10, pady=10)
        self.logout_button = Button(self.user_details_frame, text="Logout", command=self.logout)
        self.logout_button.grid(row=6, column=1, padx=10, pady=10)

        # Initialize user data
        self.name = ""
        self.age = ""
        self.salary = ""
        self.pin = ""
        self.current_balance = 0
        self.transaction_log = []
        
    def create_account(self):
        # Get user input
        name = self.name_entry.get()
        age = self.age_entry.get()
        salary = self.salary_entry.get()
        pin = self.pin_entry.get()
        
        # Validate input
        if not name or not age or not salary or not pin:
            messagebox.showerror("Error", "All fields are required!")
            return
        if not age.isdigit():
            messagebox.showerror("Error", "Age must be a number!")
            return
        if not salary.isdigit():
            messagebox.showerror("Error", "Salary must be a number!")
            return
        if not pin.isdigit() or len(pin) != 4:
            messagebox.showerror("Error", "PIN must be a 4-digit number!")
            return
        
        # Save user data
        self.name = name
        self.age = age
        self.salary = salary
        self.pin = pin
        self.current_balance = 0
        self.transaction_log = []
        
        # Clear input fields
        self.name_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.salary_entry.delete(0, END)
        self.pin_entry.delete(0, END)
        
        # Show user details
        self.name_label2.config(text="Name: " + self.name)
        self.age_label2.config(text="Age: " + self.age)
        self.salary_label2.config(text="Salary: " + self.salary)
        self.current_balance_label.config(text="Current Balance: " + str(self.current_balance))
        
        # Show user details frame
        self.create_account_frame.destroy()
        self.login_frame.pack_forget()
        self.user_details_frame.pack()


    def login(self, event=None):
        # Get user input
        pin = self.login_pin_entry.get()
        
        # Validate input
        if not pin.isdigit() or len(pin) != 4:
            messagebox.showerror("Error", "Invalid PIN!")
            return
        
        # Check PIN
        if pin != self.pin:
            messagebox.showerror("Error", "Invalid PIN!")
            return
        
        # Show user details
        self.name_label2.config(text="Name: " + self.name)
        self.age_label2.config(text="Age: " + self.age)
        self.salary_label2.config(text="Salary: " + self.salary)
        self.current_balance_label.config(text="Current Balance: " + str(self.current_balance))
        
        # Show user details frame
        self.login_frame.pack_forget()
        self.user_details_frame.pack()
    
    def deposit(self):
        # Get user input
        pin = self.login_pin_entry.get()
        amount = simpledialog.askstring("Deposit", "Enter amount:")
        
        # Validate input
        if not amount:
            return
        if not amount.isdigit() or int(amount) <= 0:
            messagebox.showerror("Error", "Invalid amount!")
            return

        # Add amount to current balance
        self.current_balance += int(amount)

        # Update current balance label
        self.current_balance_label.config(text="Current Balance: " + str(self.current_balance))

        # Add transaction to transaction log
        transaction = "Deposit: +" + amount + ", New Balance: " + str(self.current_balance)
        self.transaction_log.append(transaction)

    def withdraw(self):
        # Get user input
        pin = self.login_pin_entry.get()
        amount = simpledialog.askstring("Withdraw", "Enter amount:")
        # Validate input
        if not amount:
            return
        if not amount.isdigit() or int(amount) <= 0:
            messagebox.showerror("Error", "Invalid amount!")
            return
            
        # Check if there is enough balance
        if int(amount) > self.current_balance:
            messagebox.showerror("Error", "Insufficient balance!")
            return

        # Subtract amount from current balance
        self.current_balance -= int(amount)

        # Update current balance label
        self.current_balance_label.config(text="Current Balance: " + str(self.current_balance))

        # Add transaction to transaction log
        transaction = "Withdraw: -" + amount + ", New Balance: " + str(self.current_balance)
        self.transaction_log.append(transaction)
        
    def view_transaction_log(self):
        # Create transaction log window
        transaction_log_window = Toplevel(self.master)
        transaction_log_window.title("Transaction Log")
        # Create transaction log frame
        transaction_log_frame = Frame(transaction_log_window)
        transaction_log_frame.pack(padx=10, pady=10)

        # Create transaction log label
        transaction_log_label = Label(transaction_log_frame, text="Transaction Log:")
        transaction_log_label.grid(row=0, column=0, padx=10, pady=10)

        # Create transaction log listbox
        transaction_log_listbox = Listbox(transaction_log_frame, width=50)
        transaction_log_listbox.grid(row=1, column=0, padx=10, pady=10)

        # Insert transactions into listbox
        for transaction in self.transaction_log:
            transaction_log_listbox.insert(END, transaction)
            
    def logout(self):
        # Clear user data
        self.name = ""
        self.age = ""
        self.salary = ""
        self.pin = ""
        self.current_balance = 0
        self.transaction_log = []
        
        # Clear input fields
        self.login_pin_entry.delete(0, END)
        
        # Show login frame
        self.user_details_frame.pack_forget()
        self.login_frame.pack()

def main():
    # Create a Tk object
    root = Tk()

    # Create an instance of the BankSystem class
    bank_system = BankSystem(root)

    # Start the mainloop
    root.mainloop()

if __name__ == '__main__':
    main()
