from ManageVariables import ManageVariables

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

    def __init__(self, customer_id=1, id="", balance=0):
        self.accounts = []
        self.mv = ManageVariables()
        if id == "":
            self.id = self.assign_id()
        else:
            self.id = id
        self.customer_id = customer_id
        self.balance = balance



    def assign_id(self):
        temp_list = self.mv.get_id_list(self.accounts)
        return self.mv.get_next_id(temp_list)

    def __str__(self):
        text = "Account ID:  " + str(self.id)
        text += "\nCustomer ID:  " + str(self.customer_id)
        text += "\nBalance:  " + "${:,.2f}".format(self._balance)
        text += "\n***************************************************\n"
        return text;

