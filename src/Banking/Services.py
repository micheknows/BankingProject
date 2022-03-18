from HelperFunctions import ManageVariables

class Services:

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
    def monthly_payment(self):
        return self._monthly_payment

    @monthly_payment.setter
    def monthly_payment(self, monthly_payment):
        self._monthly_payment = monthly_payment

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, limit):
        self._limit = limit

    @property
    def num_months(self):
        return self._num_months

    @num_months.setter
    def num_months(self, num_months):
        self._num_months = num_months

    def __init__(self, id, customer_id, limit, balance):
        self.mv = ManageVariables()
        self.id = id
        self.customer_id = customer_id
        self.limit = limit
        self.balance = balance

    def deposit(self,amt):
        self.balance = self.balance + amt

    def withdraw(self, amt):
        self.balance = self.balance - amt

class credit_cards(Services):

    def calc_payment(self):
        payment = self.balance / 12.0
        if payment<25.0:
            payment = 25.0
        return payment

    def __str__(self):
        text = "Credit Card"
        text += "Credit Card ID:  " + str(self.id)
        text += "\nCustomer ID:  " + str(self.customer_id)
        text += "Credit Limit:  " + "${:,.2f}".format(self._limit)
        text += "Balance on your card:  " + "${:,.2f}".format(self._balance)
        text += "Available credit:  " + "${:,.2f}".format(self.limit - self._balance)
        text += "Next payment:  " + "${:,.2f}".format(self.calc_payment())
        text += "\n***************************************************\n"
        return text;


class Loans(Services):

    def __init__(self, id, customer_id, limit, balance, number_months):
        super().__init__(id, customer_id, limit, balance)
        self.number_months = number_months
        self.monthly_payment = self.get_monthly_payment()
        self.type = "loans"

    def get_monthly_payment(self):
        return self.limit / self.number_months

    def calc_payment(self):
        return self.balance / self.number_months

    def __str__(self):
        text = "Loan"
        text += "Loan ID:  " + str(self.id)
        text += "\nCustomer ID:  " + str(self.customer_id)
        text += "Original Loan Amount:  " + "${:,.2f}".format(self._limit)
        text += "Balance:  " + "${:,.2f}".format(self._balance)
        text += "Number of Months:  " + "${:,.2f}".format(self.number_months)
        text += "Monthly Payment Amount:  " + "${:,.2f}".format(self.calc_payment())
        text += "\n***************************************************\n"
        return text;

