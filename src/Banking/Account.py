from Customer import Customer

class Account:

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, at):
        self._account_type = at

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        self._customer = customer

    def transaction(self, desc, amt):
        self.balance = self.balance + amt
        print("Transaction:  " + desc)
        print("New balance is:  $" + self.format_money(self.balance) )

    def __init__(self, id, customer, account_type, balance):
        self.account_types = {"c": "checking", "s" : "savings"}
        self.id = id
        self.customer = customer
        self.account_type = account_type
        self.balance = balance

    def __str__(self):
        text = "\n\nAccount"
        text = text + "  ID:  " + str(self.id) + "\n"
        text = text + "Customer :  " + self.customer.fname + " " + self.customer.lname +  "\n"
        text = text + "Customer ID:  " + str(self.customer.id) + "\n"
        text = text + "Account Type:  " + self.account_types[self.account_type] + "\n"
        text = text + "Balance:  $" + self.format_money(self.balance) + "\n"
        return text

    def format_money(self, amt):
        return str(amt)