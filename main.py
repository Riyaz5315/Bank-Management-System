from register import *
from bank import *
from account_closing import BankManagementSystem  # Import the class from account_closing.py

def print_header(title):
    print("\n" + "="*50)
    print(f"{title:^50}")
    print("="*50)

def print_message(message):
    print(f"\n{message}\n")
    
def admin_login():
    # Admin credentials can be hardcoded or fetched from a database
    admin_user = "admin"
    admin_pass = "admin123"
    
    while True:
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if username == admin_user and password == admin_pass:
            print_message("Admin login successful!")
            return True
        else:
            print_message("Invalid admin credentials. Please try again.")

def view_all_customers():
    # Adjusted query to match the actual columns in the 'customers' table
    customers = db_query("SELECT account_number, username, name, age, city, balance FROM customers;")
    
    if customers:
        print_header("All Customer Details")
        for customer in customers:
            account_number = customer[0]
            username = customer[1]
            name = customer[2]  # The 'name' field
            age = customer[3]
            city = customer[4]
            balance = customer[5]

            print(f"Account Number: {account_number}")
            print(f"Username: {username}")
            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"City: {city}")
            print(f"Balance: {balance}")
            print("-" * 50)
    else:
        print_message("No customer records found.")


def close_customer_account():
    account_number = input("Enter the account number of the customer to close: ")
    confirm = input(f"Are you sure you want to close the account {account_number}? (yes/no): ").lower()
    
    if confirm == "yes":
        try:
            # Assuming you have a cursor for executing queries
            cursor.execute(f"DELETE FROM customers WHERE account_number = '{account_number}'")
            mydb.commit()  # Commit the transaction
            print_message(f"Account {account_number} has been successfully closed and removed from the system.")
        except Exception as e:
            print_message(f"Error occurred while closing the account: {str(e)}")
    else:
        print_message("Account closure cancelled.")



# Main Program
print_header("Welcome to the Banking Project")

status = False
is_admin = False

while True:
    try:
        register = int(input("Please choose an option:\n"
                             "1. SignUp\n"
                             "2. SignIn (Customer)\n"
                             "3. Admin Login\n"
                             "Enter your choice (1, 2, or 3): "))
                             
        if register == 1:
            SignUp()
        elif register == 2:
            user = SignIn()
            status = True
            break
        elif register == 3:
            if admin_login():
                is_admin = True
                break
        else:
            print_message("Invalid input. Please enter 1 for SignUp, 2 for Customer SignIn, or 3 for Admin Login.")
    except ValueError:
        print_message("Invalid input. Please enter a number.")

# Admin Dashboard
if is_admin:
    while True:
        print_header("Admin Dashboard")
        admin_choice = int(input("1. View All Customers\n"
                                 "2. Close Customer Account\n"
                                 "3. Exit\n"
                                 "Enter your choice (1-3): "))
        
        if admin_choice == 1:
            view_all_customers()
        elif admin_choice == 2:
            close_customer_account()
        elif admin_choice == 3:
            print_message("Admin logged out.")
            break
        else:
            print_message("Invalid input. Please enter 1, 2, or 3.")

# Customer Service
else:
    account_number = db_query(
        f"SELECT account_number FROM customers WHERE username = '{user}';")[0][0]

    while status:
        print_header(f"Welcome {user.capitalize()}! Choose Your Banking Service")
        
        try:
            facility = int(input("1. Balance Enquiry\n"
                                 "2. Cash Deposit\n"
                                 "3. Cash Withdraw\n"
                                 "4. Fund Transfer\n"
                                 "5. Exit\n"
                                 "Enter your choice (1-5): "))

            if facility == 1:
                bobj = Bank(user, account_number)
                bobj.balanceequiry()

            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter the amount to deposit: "))
                        bobj = Bank(user, account_number)
                        bobj.deposit(amount)
                        mydb.commit()
                        print_message(f"Successfully deposited {amount}.")
                        break
                    except ValueError:
                        print_message("Invalid input. Please enter a number.")

            elif facility == 3:
                while True:
                    try:
                        amount = int(input("Enter the amount to withdraw: "))
                        bobj = Bank(user, account_number)
                        bobj.withdraw(amount)
                        mydb.commit()
                        print_message(f"Successfully withdrew {amount}.")
                        break
                    except ValueError:
                        print_message("Invalid input. Please enter a number.")

            elif facility == 4:
                while True:
                    try:
                        receive = int(input("Enter the receiver account number: "))
                        amount = int(input("Enter the amount to transfer: "))
                        bobj = Bank(user, account_number)
                        bobj.fundtransfer(receive, amount)
                        mydb.commit()
                        print_message(f"Successfully transferred {amount} to account {receive}.")
                        break
                    except ValueError:
                        print_message("Invalid input. Please enter numbers.")

            elif facility == 5:
                print_message("Thank you for using our banking services!")
                status = False

            else:
                print_message("Invalid input. Please enter a number between 1 and 5.")

        except ValueError:
            print_message("Invalid input. Please enter a number.")
