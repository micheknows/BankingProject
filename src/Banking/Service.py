from HelperFunctions import HelperFunctions


class Service:

    def __init__(self, service_id, customer_id, customers, balance):
        self.service_id = service_id
        self.customer_id = customer_id
        self.balance = balance
        self.customers = customers
        self.approved = False
        self.denied = False

    def denied(self, reason):
        self.reason = reason
        self.balance = 0

    def approval_message(self):
        if not self.approved:
            if not self.denied:
                text = "\n\nYOUR APPLICATION FOR THE FOLLOWING IS PROCESSING.  WE WILL INFORM YOU OF OUR CREDIT DECISION.\n\n"
            else:
                text = "\n\nWe are sorry to inform you that this applicaton was denied.\n\n"
        return "" if self.approved else text

class Loan(Service):

    def __init__(self, service_id, customer_id, amount, customers, purpose):
        super().__init__(service_id, customer_id, customers, amount)
        self.purpose = purpose
        self.orig_loan_amount = amount

    def deny(self, reason):
        super().denied(reason)
        self.orig_loan_amount = 0

    def __str__(self):
        text = super().approval_message()
        text = text + "\n\n**********\n\nLOAN ID:  " + str(self.service_id)
        text = text + "\nCustomer:  " + self.customers.get_name_by_id(self.customer_id)
        text = text + "\nPurpose:  " + self.purpose
        text = text + "\nOriginal Loan Amount:  $" + HelperFunctions.format_currency(self.orig_loan_amount)
        text = text + "\nBalance:  $" + HelperFunctions.format_currency(self.balance)
        return text

class CreditCard(Service):

    def __init__(self, service_id, customer_id, amount, customers):
        super().__init__(service_id, customer_id, customers, 0)
        self.limit = amount

    def deny(self, reason):
        super().denied(reason)
        self.limit = 0

    def __str__(self):
        text = super().approval_message()
        text = text + "\n\n**********\n\nCREDIT CARD ID:  " + str(self.service_id)
        text = text + "\nCustomer:  " + self.customers.get_name_by_id(self.customer_id)
        text = text + "\nCredit Limit:  $" + HelperFunctions.format_currency(self.limit)
        text = text + "\nBalance:  $" + HelperFunctions.format_currency(self.balance)
        return text

