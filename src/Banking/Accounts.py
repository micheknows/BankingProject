from HelperFunctions import HelperFunctions
from Account import Account

class Accounts:

    def __init__(self):
        self.accounts = []
        self.account_types = ["checking", "savings"]

    def create_account(self, customers):
        cid_list = [c.id for c in customers.customers]
        customer_id = HelperFunctions.get_valid_id(cid_list, "Enter the customer id for which you wish to create an account:  ")
        if customer_id>0:
            id = HelperFunctions.get_next_id([account.id for account in self.accounts])
            account_type = HelperFunctions.get_string_from_list([s[0] for s in self.account_types],"Enter the first letter of the account type " + repr(self.account_types) + ":  ")
            if account_type != "@":
                balance = HelperFunctions.get_float("What is the opening deposit amount:  ")
                self.accounts.append(Account(id, customer_id, [s for s in self.account_types if s.startswith(account_type.lower())][0],balance, customers))
                print("Account created")
                print(self.accounts[len(self.accounts)-1])

    def get_account_list_by_customer_id(self, customer_id):
        return [account for account in self.accounts if account.customer_id == customer_id]

    def view_account_list(self, account_list):
        if len(account_list)>0:
            for account in account_list:
                print(account)
        else:
            print("No accounts for this customer.")