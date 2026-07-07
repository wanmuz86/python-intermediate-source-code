# Aggregation class to manage the accounts
# 1 Bank has Many accounts
# The account is managed by key -> account_no
import shelve

class Bank:
    def __init__(self):
        self.accounts = {} #1 to many relation in DB , UML -> Aggregation

    def add_account(self,account):
        # Save the account using key= account_no
        #  {"E101":{account_no:"E101",name:"Aina",amount:100},
        #  "E102":{account_no:"E102",name:"John",amount:1000} }
        self.accounts[account.account_no] = account
    
    def get_account(self,account_no):
       # return self.accounts[account_no]
       # print(accounts["E101"])
        return self.accounts.get(account_no)

    def list_accounts(self):
        print("\n---Account List--")
        # For loop in dictionary (values())
        for acc in self.accounts.values():
            print(acc.get_summary)


    # Save and Retrieve from db (shelve)

    def save_to_db(self, filename="bank_db"):
        with shelve.open(filename) as db:
            # Go through all the key and value in accounts dictionary
            # key -> acc_no
            # value -> acc
            for acc_no, acc in self.accounts.items():
                # save it in db using key-value
                db[acc_no] = acc       # save based on key
    
    def load_from_db(self, filename="bank_db"):
        with shelve.open(filename) as db:
            for key in db:
                self.accounts[key] = db[key] #retrive based on key