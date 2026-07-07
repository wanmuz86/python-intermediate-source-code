class Account:
    
    # balance = 0 , defaulted at 0 if it is not specified
    def __init__(self, account_no, owner, balance=0):
        self.account_no = account_no
        self.owner = owner
        self.balance = balance
    
    # Add amount in bank account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    # Remove a certain amount from bank account
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance- amount
        else:
            print("Insufficient fund")

    def get_summary(self):
        return f"{self.no_account} | {self.owner} | Balance: {self.balance}"