from ManageVariables import ManageVariables
from Customers import Customers
from AccountFunctions import AccountFunctions


def current_id(self):
    return self._current_id


@current_id.setter
def current_id(self, id):
    self._current_id = current_id

class CustomerFunctions:

    def __init__(self):
        self.customers = []
        self.read()
        self.currentID = None
        self.af = AccountFunctions()
        self.mv = ManageVariables()

    def customer_application_menu(self):
        menu_choices = {
            "View My Profile" : self.view_my_profile,
            "View My Accounts" : self.view_my_accounts,
            "Make Deposit" : lambda : self.make_transaction("depositing"),
            "Make Withdrawal" : lambda : self.make_transaction("withdrawing")
        }
        menu_location = "customer application"
        return menu_choices, menu_location

    def view_my_accounts(self):
        while self.currentID==None:
            self.currentID = self.mv.askQuestion("Please enter your ID:  ")
        print(str(self.af.get_customer_accounts(self.currentID)))

    def view_my_profile(self):
        while self.currentID==None:
            self.currentID = self.mv.askQuestion("Please enter your ID:  ")
        print(str(self.get_customer_by_id(self.currentID)))

    def make_transaction(self, transaction):
        while self.currentID==None:
            self.currentID = self.mv.askQuestion("Please enter your ID:  ")
        if len(self.af.get_customer_accounts(self.currentID))<1:
            print("Sorry, you do not have any accounts to use.")
        else:
            print("Your active accounts are:  ")
            print(str(self.af.get_customer_accounts(self.currentID)))
            while True:
                try:
                    account_id =int(self.mv.askQuestion("What is the account number?"))
                    if account_id in self.af.get_list_account_ids_by_customer_id(self.currentID) or account_id==0:
                        break
                except:
                    print("Please try again.  That is not a valid account number. (or enter 0 to cancel the deposit)")
            while True and account_id!=0:
                try:
                    text = "How much are you " + transaction + "?"
                    transaction_amt = float(self.mv.askQuestion(text))
                    break
                except:
                    print("Please try again.  You must enter a numerical amount. (or enter 0 to cancel the transaction)")
            if account_id!=0:
                if transaction=="withdrawing":
                    if self.af.accounts[self.af.get_index_by_account_id(self.currentID)].balance < deposit:
                        print("You do not have that much to withdraw.")
                    else:
                        deposit = deposit * -1
                        return False
                self.af.deposit(account_id,deposit)
                print("You were " + transaction + " + "${:,.2f}".format(deposit) + "    account #" + str(account_id) + ".")
                print(str(self.af.accounts[self.af.get_index_by_account_id(account_id)]))
            return True

    def createCustomer(self, firstname, lastname, address):
        self.customers.append(Customers(firstname, lastname, address))
        print(str(self.customers[len(self.customers)-1]))
        self.save()

    def get_index_by_id(self, customer_id):
        for index, i in enumerate(self.customers):
            if i.id==customer_id:
                return index


    def get_customer_by_id(self, customer_id):
        customer = [customer for customer in self.customers if customer.id==customer_id][0]
        return customer

    def save(self):
        templist = [[item.id, item.firstname, item.lastname, item.address] for item in self.customers]
        self.mv.save_variables(templist,"customers")

    def read(self):
        templist = self.mv.read("customers")
        customers = [[int(item[0]), item[1], item[2], item[3]] for item in templist if len(item)>0]
        for customer in customers:
            self.customers.append(Customers(customer[1], customer[2], customer[3], customer[0]))

