from ManageVariables import ManageVariables
from CustomerFunctions import CustomerFunctions
from AccountFunctions import AccountFunctions

class EmployeesFunctions:

    def __init__(self):
        self.mv = ManageVariables()
        self.cf = CustomerFunctions()
        self.currentID = None
        self.af = AccountFunctions()

    def employee_application_menu(self):
        menu_choices = {
            "View All Customers" : self.view_customers,
            "Create A Customer" : self.create_customer,
            "View Account For A Customer" : self.view_one_customer_account,
            "Add Fee to Customer Account" : self.add_fee
        }
        menu_location = "Employee Application"
        return menu_choices, menu_location

    def view_one_customer_account(self):
        while self.currentID==None:
            self.currentID = int(self.mv.askQuestion("Please enter the customer ID:  "))
        if self.cf.get_index_by_id(self.currentID)>-1:
            for account in self.af.get_customer_accounts(self.currentID):
                print(str(account))
        else:
            print("That is not a valid customer ID.")
        self.currentID = None

    def add_fee(self):
        while self.currentID==None:
            self.currentID = int(self.mv.askQuestion("Please enter the account ID:  "))
        if self.af.get_index_by_account_id(self.currentID)>-1:
            while True:
                try:
                    amt = float(self.mv.askQuestion("How much is the fee?"))
                    break
                except:
                    print("Please try again, your entry must be a number.")
            desc = self.mv.askQuestion("What is the description of the fee?")
            self.af.add_fee(self.currentID, amt, desc)
        else:
            print("That is not a valid account ID.")
        self.currentID = None


    def view_customers(self):
        for customer in self.cf.customers:
            print(str(customer))


    def create_customer(self):
        firstname = self.mv.askQuestion("Enter customer first name")
        lastname = self.mv.askQuestion("Enter customer last name")
        address = self.mv.askQuestion("Enter customer address")
        self.cf.createCustomer(firstname, lastname, address)
        print("Customer created")
