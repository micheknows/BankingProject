from HelperFunctions import ManageVariables
from Accounts import Accounts

class AccountFunctions:

    def __init__(self):
        self.accounts = []
        self.read()

    def createAccount(self, customer_id,account_type, balance=0):
        self.accounts.append(Accounts(customer_id, balance, account_type))
        print(str(self.accounts[len(self.accounts)-1]))
        self.save()

    def get_customer_accounts(self, customer_id):
        caccounts = [account for account in self.accounts if account.customer_id==customer_id]
        return caccounts

    def add_fee(self, account_id, fee_amt, fee_desc):
        print(str(self.accounts[self.get_index_by_account_id(account_id)]))
        self.accounts[self.get_index_by_account_id(account_id)].withdraw(fee_amt)
        print("Fee of " + "${:,.2f}".format(fee_amt) + " assessed for:  " + fee_desc + "\n")
        print(str(self.accounts[self.get_index_by_account_id(account_id)]))

    def get_index_by_account_id(self, account_id):
        for index, i in enumerate(self.accounts):
            if i.id==account_id:
                return index
        return -1

    def get_list_account_ids_by_customer_id(self, customer_id):
        return [item.id for item in self.accounts if item.customer_id==customer_id]

    def deposit(self,account,amt):
        account.deposit(amt)

    def withdraw(self, account):
        account.depsit(amt)

    def save(self):
        templist = [[item.id, item.customer_id, item.account_type, item.balance] for item in self.accounts]
        mv = ManageVariables()
        mv.save_variables(templist,"accounts")

    def read(self):
        mv = ManageVariables()
        templist = mv.read("accounts")
        accounts = [[int(item[0]), int(item[1]), item[2], float(item[3])] for item in templist if len(item)>0]
        for account in accounts:
            self.accounts.append(Accounts(account[1], account[3], account[2], account[0]))



