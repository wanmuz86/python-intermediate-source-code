from account import Account

class CurrentAccount(Account):
    
    # Create an initializer with overdraft (- amount allowed)
    def __init__(self, account_no,owner, balance, overdraft_limit):
        super().__init__(account_no,owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            self.add_history("WITHDRAW", amount)
        else:
            print("Overdraft limit exceeded")
            self.add_history("WITHDRAW FAILED", amount)

    