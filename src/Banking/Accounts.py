from HelperFunctions import HelperFunctions
from Account import Account
from Data import Data


# noinspection PyArgumentList
class Accounts:

    def __init__(self):
        self.accounts = Data.retrieve_data("accounts")
        self.account_types = ["checking", "savings"]

    def get_valid(valid):
        def decorator(fn):
            def decorated(*args, **kwargs):
                if 'customer' in valid:
                    customer_id = Accounts.get_valid_customer(kwargs['customers'])
                    if customer_id > 0:
                        if 'account' in valid:
                            account_id = Accounts.get_valid_account_by_customer_id(args[0], customer_id)
                            if account_id > 0:
                                fn(customer_id=customer_id, account_id=account_id, *args, **kwargs)
                        else:
                            fn(customer_id=customer_id, *args, **kwargs)
            return decorated
        return decorator

    def get_valid_account_by_customer_id(accounts, customer_id):
        aid_list = [a.id for a in accounts.accounts if a.customer_id == customer_id]
        print("Here are the customer's accounts:")
        for account in accounts.get_account_list_by_customer_id(customer_id):
            print(str(account))
        if len(accounts.get_account_list_by_customer_id(customer_id)) < 1:
            print("There are no valid accounts for this customer.")
            return 0
        else:
            account_id = HelperFunctions.get_valid_id(aid_list, "Enter the id for the customer's account:  ")
            return account_id

    def get_valid_customer(customers):
        cid_list = [c.id for c in customers.customers]
        print("Here are the active customers:")
        for customer in customers.customers:
            print(str(customer))
        if len(customers.customers) < 1:
            print("There are no valid customers at this bank.")
            return 0
        else:
            customer_id = HelperFunctions.get_valid_id(cid_list, "Enter the customer id for the account:  ")
            return customer_id

    @get_valid(['customer'])
    def create_account(self, customer_id="", customers=()):
        account_id = HelperFunctions.get_next_id([account.id for account in self.accounts])
        account_type = HelperFunctions.get_string_from_list([s[0] for s in self.account_types],"Enter the first "
                                                                                               "letter of the account"
                                                                                               " type " + repr(
            self.account_types) + ":  ")
        if account_type != "@":
            balance = HelperFunctions.get_float("What is the opening deposit amount:  ")
            type_of_account = [s for s in self.account_types if s.startswith(account_type.lower())][0]
            self.accounts.append(Account(account_id, customer_id, type_of_account,balance, customers))
            print("Account created")
            print(self.accounts[len(self.accounts)-1])
            self.save()

    @get_valid(['customer', 'account'])
    def add_fee(self, customer_id="", account_id="", customers=()):
        desc = HelperFunctions.get_string("What is the fee for?")
        amt = HelperFunctions.get_float("How much is the fee?")
        print(str(self.get_account_by_id(account_id)))
        print("\n\nFee Assessed for:  " + desc)
        print("\nFee Amount:  " + HelperFunctions.format_currency(amt))
        print("\nPrevious Balance:  " + HelperFunctions.format_currency(self.get_account_by_id(account_id).balance))
        self.get_account_by_id(account_id).balance = self.get_account_by_id(account_id).balance - amt
        print("\nCurrent Balance:  " + HelperFunctions.format_currency(self.get_account_by_id(account_id).balance))

    def transaction(self, account_id, amt):
        self.get_account_by_id(account_id).balance = self.get_account_by_id(account_id).balance + amt
        self.save()

    def get_account_by_id(self, account_id):
        return [a for a in self.accounts if a.id == account_id][0]

    def get_account_list_by_customer_id(self, customer_id):
        return [account for account in self.accounts if account.customer_id == customer_id]

    def view_account_list(self, account_list):
        if len(account_list) > 0:
            for account in account_list:
                print(account)
        else:
            print("No accounts for this customer.")

    def save(self):
        Data.save_data(self.accounts, "accounts")
