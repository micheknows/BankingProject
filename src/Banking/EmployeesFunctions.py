from HelperFunctions import ManageVariables
from CustomerFunctions import CustomerFunctions
from AccountFunctions import AccountFunctions
from ServiceFunctions import ServiceFunctions

class EmployeesFunctions:

    def __init__(self):
        self.sf = ServiceFunctions()
        self.mv = ManageVariables()
        self.cf = CustomerFunctions()
        self.currentID = None
        self.af = AccountFunctions()

    def employee_application_menu(self):
        menu_choices = {
            "View All Customers" : self.view_customers,
            "Create A Customer" : self.create_customer,
            "Create Customer Account" : self.create_account,
            "View Account For A Customer" : self.view_one_customer_account,
            "Add Fee to Customer Account" : self.add_fee,
            "Create Customer Loan" : self.create_loan
        }
        menu_location = "Employee Application"
        return menu_choices, menu_location

    def create_loan(self):
        id = self.cf.get_valid_customer()
        if id>-1:
            limit = -1
            while limit < 0:
                try:
                    limit = float(self.mv.askQuestion("What is the amount of the loan?"))
                except ValueError:
                    print("Please try again.  The amount must be a number.")
            balance = 0
            number_months = -1
            while number_months < 0:
                try:
                    number_months = int(self.mv.askQuestion("For how many months?"))
                except ValueError:
                    print("Please try again.  The number of months must be a number.")
            self.sf.createLoan(customer_id, limit, balance, number_months )
            print("Loan Created.")

    def create_account(self):
        account_type_list = ["Savings","Checking"]
        id = self.cf.get_valid_customer()
        if id>-1:
            account_type = "a"
            while account_type.lower() not in ["c", "s"]:
                account_type = self.mv.askQuestion("Enter the account type (c = checking or s = savings):  ")
            deposit = -1
            while deposit < 0:
                try:
                    deposit = float(self.mv.askQuestion("What is the initial deposit amount?"))
                except ValueError:
                    print("Please try again.  The initial deposit must be a number.  If there is no deposit, enter 0.")
            self.af.createAccount(id, [item for item in account_type_list if item[0].lower()==account_type][0], deposit)
            print("Account Created.")

    def create_load(self):
        pass

    def view_one_customer_account(self):
        id = self.cf.get_valid_customer()
        if id>-1:
            for account in self.af.get_customer_accounts(id):
                print(str(account))

    def add_fee(self):
        id = self.af.get_valid_account()
        if id>-1:
            while True:
                try:
                    amt = float(self.mv.askQuestion("How much is the fee?"))
                    break
                except:
                    print("Please try again, your entry must be a number.")
            desc = self.mv.askQuestion("What is the description of the fee?")
            self.af.add_fee(id, amt, desc)


    def view_customers(self):
        for customer in self.cf.customers:
            print(str(customer))


    def create_customer(self):
        firstname = self.mv.askQuestion("Enter customer first name")
        lastname = self.mv.askQuestion("Enter customer last name")
        address = self.mv.askQuestion("Enter customer address")
        self.cf.createCustomer(firstname, lastname, address)
        print("Customer created")
