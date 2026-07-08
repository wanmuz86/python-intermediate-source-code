from account import Account
class SavingsAccount(Account):
    
    def __init__(self, account_no, owner, balance, interest_rate):
        # Calling the parent's  constructor
        super().__init__(account_no, owner,balance)
        # add also interest_rate property
        self.interest_rate = interest_rate

    def apply_interest(self):
        # call the menthod round(XX, 2) -> To round to 2 decimal point
        interest = round(self.balance * self.interest_rate,2)
        self.balance +=  interest
        self.add_history("INTEREST", interest)
