from account import Account
from bank import Bank
from savings_account import SavingsAccount
from current_account import CurrentAccount

# Utiliy methods to investigate, troubleshoot our object
def inspect_object(obj):
    print("\n-- Object Inspection --")
    print("Type: ", type(obj)) # Type of object -> class name
    print("Attributes:", vars(obj)) # Bring out the attributes (method + property)

    methods = [
        name for name in dir(obj) # list all method, property and dunder method
        # callable -> Can be executed
        if callable(getattr(obj,name)) and not name.startswith("__") #to list down all the methods of the object
    ]
    print("Methods", methods)


# a = Account("A100", "Aina", 100)
# a.deposit(50)
# a.withdraw(30)
# print(a.get_summary())

def main():
    bank = Bank()
    bank.load_from_db() # Get from DB

    if not bank.accounts:  # If no data
        # Create a mock data
        #Creating new account using constructor
        # Add the account to accounts collenction in bank
        bank.add_account(SavingsAccount("S200","Ali",200,0.05))
        bank.add_account(CurrentAccount("C300", "Mira", 50, overdraft_limit=100))
    
    acc = bank.get_account("S200")
    acc.deposit(20)

    # Check if there is method apply_interest
    # If it is CurrentAccount => False
    if hasattr(acc, "apply_interest"):
        acc.apply_interest()
    
    inspect_object(acc)
    
    # Print the transaction history of Ali's account
    acc.print_history()

    bank.save_to_db()

    # Ali and Mira's account
    bank.list_accounts()

if __name__ == "__main__":
    main()