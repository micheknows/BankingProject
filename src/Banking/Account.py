from Customers import Customers
from HelperFunctions import HelperFunctions

class Account:


    def __init__(self, id, customer_id, account_type, balance, customers):
        self.id = id
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = balance
        self.customers = customers

    def __str__(self):
        text = "\n\n**********\n\nACCOUNT ID:  " + str(self.id)
        text = text + "\nCustomer:  " + self.customers.get_name_by_id(self.customer_id)
        text = text + " \nAccount Type:  " + self.account_type
        text = text + "\nBalance:  $" + HelperFunctions.format_currency(self.balance)
        return text

