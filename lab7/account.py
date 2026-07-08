from datetime import datetime

class Account:
    
    # balance = 0 , defaulted at 0 if it is not specified
    def __init__(self, account_no, owner, balance=0):
        self.account_no = account_no
        self.owner = owner
        self.balance = balance
        self.history = [] # To keep track of all the transactions
        self.add_history("OPEN", balance) #Show the opening balance
    

    # Method to add all actions inside history / transaction history

    def add_history(self, action, amount):
        # add at the end of list -> append
        self.history.append({
            "time":datetime.now().isoformat(timespec="seconds"),
            "action":action,
            "amount":float(amount), #transform int or string into float
            "balance":float(self.balance)
        })
    
    # Add amount in bank account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

        self.add_history("DEPOSIT", amount)

    # Remove a certain amount from bank account
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance- amount
            self.add_history("WITHDRAW", amount)
        else:
            print("Insufficient fund")
            self.add_history("WITHDRAW FAILED",amount)

    def get_summary(self):
        return f"{self.account_no} | {self.owner} | Balance: {self.balance}"

# to show the transaction history for given account
    def print_history(self):
        print(f"\n-- Transaction History: {self.account_no} --")
        for h in self.history:
            print(f"{h['time']} | {h['action']} | amount={h['amount']}| balance={h['balance']}")