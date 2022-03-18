from HelperFunctions import ManageVariables
from Customers import Customers
from AccountFunctions import AccountFunctions
from ServiceFunctions import ServiceFunctions

@property
def current_id(self):
    return self._current_id


@current_id.setter
def current_id(self, id):
    self._current_id = current_id

class CustomerFunctions:

    def __init__(self):
        self.mv = ManageVariables()
        self.customers = []
        self.read()
        self.currentID = None
        self.af = AccountFunctions()
        self.sf = ServiceFunctions()

    def customer_application_menu(self):
        menu_choices = {
            "View My Profile" : self.view_my_profile,
            "View My Accounts" : self.view_my_accounts,
            "Make Deposit" : lambda : self.make_transaction("depositing"),
            "Make Withdrawal" : lambda : self.make_transaction("withdrawing"),
            "View my Loans" : self.view_loans,
            "View my Credit Cards" : self.view_ccs
        }
        menu_location = "Customer Application"
        return menu_choices, menu_location

    def view_my_accounts(self):
        while self.currentID==None:
            self.currentID = self.mv.askQuestion("Please enter your ID:  ")
        if self.get_index_by_id(self.currentID)>-1:
            for account in self.af.get_customer_accounts(self.currentID):
                print(str(account))
        else:
            print("Sorry, that ID is not a customer of this bank.")

    def view_loans(self):
        while self.currentID==None:
            self.currentID = self.mv.askQuestion("Please enter your ID:  ")
        if self.get_index_by_id(self.currentID)>-1:
            for loan in self.sf.get_customer_loans(self.currentID):
                print(str(loan))
        else:
            print("Sorry, that ID is not a customer of this bank.")

    def view_ccs(self):
        while self.currentID==None:
            self.currentID = self.mv.askQuestion("Please enter your ID:  ")
        if self.get_index_by_id(self.currentID)>-1:
            for cc in self.sf.get_customer_ccs(self.currentID):
                print(str(cc))
        else:
            print("Sorry, that ID is not a customer of this bank.")

    def view_my_profile(self):
        self.currentID = self.get_valid_customer(self.currentID)
        if self.currentID>-1:
            print(str(self.get_customer_by_id(self.currentID)))

    def make_transaction(self, transaction):
        self.currentID = self.get_valid_customer(self.currentID)
        if self.currentID>-1:
            if len(self.af.get_customer_accounts(self.currentID))<1:
                print("Sorry, that ID does not have any accounts to use.")
            else:
                print("Active accounts are:  ")
                self.af.print_account_list(self.af.get_customer_accounts(self.currentID))
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
                        if self.af.accounts[self.af.get_index_by_account_id(self.currentID)].balance < transaction_amt:
                            print("You do not have that much to withdraw.")
                            return False
                        else:
                            transaction_amt = transaction_amt * -1
                    self.af.deposit(self.af.get_account_by_account_id(account_id),transaction_amt)
                    print("You were " + transaction +  " ${:,.2f}".format(transaction_amt) + "   :  Account #" + str(account_id) + ".")
                    print(str(self.af.accounts[self.af.get_index_by_account_id(account_id)]))
                return True

    def createCustomer(self, firstname, lastname, address):
        self.customers.append(Customers(firstname, lastname, address,self.assign_id()))
        print(str(self.customers[len(self.customers)-1]))
        self.save()

    def assign_id(self):
        temp_list = self.mv.get_id_list(self.customers)
        return self.mv.get_next_id(temp_list)

    def get_index_by_id(self, customer_id):
        for index, i in enumerate(self.customers):
            if i.id==customer_id:
                return index
        return -1

    def get_valid_customer(self, id=None):
        while id==None:
            id = int(self.mv.askQuestion("Please enter the customer ID:  "))
        if self.get_customer_by_id(id):
            return id
        else:
            print("That is not a valid customer ID.")
            return -1



    def get_customer_by_id(self, customer_id):
        try:
            customer = [customer for customer in self.customers if customer.id==customer_id][0]
        except IndexError:
            customer = None
        return customer

    def save(self):
        templist = [[item.id, item.firstname, item.lastname, item.address] for item in self.customers]
        self.mv.save_variables(templist,"customers")

    def read(self):
        templist = self.mv.read("customers")
        customers = [[int(item[0]), item[1], item[2], item[3]] for item in templist if len(item)>0]
        for customer in customers:
            self.customers.append(Customers(customer[1], customer[2], customer[3], customer[0]))

