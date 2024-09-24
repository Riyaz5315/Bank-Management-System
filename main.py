from register import *
from bank import *
from account_closing import BankManagementSystem  # Import the class from account_closing.py

def print_header(title):
    print("\n" + "="*50)
    print(f"{title:^50}")
    print("="*50)

def print_message(message):
    print(f"\n{message}\n")

print_header("Welcome to the Banking Project")

status = False

while True:
    try:
        register = int(input("Please choose an option:\n"
                             "1. SignUp\n"
                             "2. SignIn\n"
                             "Enter your choice (1 or 2): "))
                             
        if register == 1:
            SignUp()
        elif register == 2:
            user = SignIn()
            status = True
            break
        else:
            print_message("Invalid input. Please enter 1 for SignUp or 2 for SignIn.")
    except ValueError:
        print_message("Invalid input. Please enter a number.")

account_number = db_query(
    f"SELECT account_number FROM customers WHERE username = '{user}';")[0][0]

while status:
    print_header(f"Welcome {user.capitalize()}! Choose Your Banking Service")
    
    try:
        facility = int(input("1. Balance Enquiry\n"
                             "2. Cash Deposit\n"
                             "3. Cash Withdraw\n"
                             "4. Fund Transfer\n"
                             "5. Close Account (Permanently)\n"
                             "6. Exit\n"
                             "Enter your choice (1-6): "))

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
            confirm = input(f"Are you sure you want to close your account, {user.capitalize()}? (yes/no): ").lower()
            if confirm == "yes":
                bank_system = BankManagementSystem(user)
                bank_system.close_account()
                print_message("Your account has been closed successfully.")
                status = False
            else:
                print_message("Account closure cancelled.")

        elif facility == 6:
            print_message("Thank you for using our banking services!")
            status = False

        else:
            print_message("Invalid input. Please enter a number between 1 and 6.")

    except ValueError:
        print_message("Invalid input. Please enter a number.")
