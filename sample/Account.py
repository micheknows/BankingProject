class Account:

    def __init__(self, banking, id, customer_id=0, account_type="", balance=0):
        self._id = id
        self._customer_id = customer_id
        self._account_type = account_type
        self._balance = balance
        self.banking = banking

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, name):
        self._customer_id = name

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, name):
        self._account_type = name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, add):
        self._balance = add

    def __repr__(self):
        text = "Account ID:  " + str(self._id) + "\nCustomer:  " + self.banking.customers.customers[self.banking.customers.get_by_id(self._customer_id)].first_name + " " + self.banking.customers.customers[self.banking.customers.get_by_id(self._customer_id)].last_name
        text += "\nAccount Type:  " + self._account_type
        text += "\nBalance:  " + "${:,.2f}".format(self._balance)
        return text