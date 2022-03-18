from HelperFunctions import ManageVariables

class Accounts:

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self._customer_id = customer_id

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        self._account_type = account_type

    def __init__(self, customer_id=1, balance=0, account_type="checking", id=""):
        self.mv = ManageVariables()
        if id == "":
            self.id = self.assign_id()
        else:
            self.id = id
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = balance

    def deposit(self,amt):
        self.balance = self.balance + amt

    def withdraw(self, amt):
        self.balance = self.balance - amt


    def __str__(self):
        text = "Account ID:  " + str(self.id)
        text += "\nCustomer ID:  " + str(self.customer_id)
        text += "\nAccount type:  " + str(self.account_type)
        text += "\nBalance:  " + "${:,.2f}".format(self._balance)
        text += "\n***************************************************\n"
        return text;

