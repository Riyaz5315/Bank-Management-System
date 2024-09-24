from database import db_query, mydb

class BankManagementSystem:

    def __init__(self, username):
        self.username = username

    def close_account(self):
        try:
            # Query to delete the customer from the database
            db_query(f"DELETE FROM customers WHERE username = '{self.username}';")
            mydb.commit()
            print(f"Account with username '{self.username}' has been permanently closed.")
        except Exception as e:
            print(f"An error occurred while closing the account: {str(e)}")


# Example usage
if __name__ == "__main__":
    username = input("Enter the username of the account to close: ")
    bank_system = BankManagementSystem(username)
    bank_system.close_account()

   
