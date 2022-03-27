from Customers import Customers
from HelperFunctions import HelperFunctions


class Account:
    """
    A class to represent an account

    ...

    Attributes
    -----------
    id : int
        the identification for the account
    customer_id : int
        the id for the customer associated with the account
    account_type : str
        whether the account is checking or savings
    balance : float
        how much money is currently in the account

    Methods
    ---------
    __str__():
        returns a user-friendly string representation of the account object

    """

    def __init__(self, account_id, customer_id, account_type, balance):
        """
        Constructs all the necessary attributes for the account object

        Parameters
        -----------
            account_id : int
                the identification for the account
            customer_id : int
                the id for the customer associated with the account
            account_type : str
                whether the account is checking or savings
            balance : float
                how much money is currently in the account


        """
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = balance

    def __str__(self):
        """
        returns a user-friendly string representation of the account

        Parameters
        -------------
        None

        Returns
        -------------
        text    :   str
            user-friendly string of the attributes of the account object

        """
        customers = Customers()
        text = "\n\n**********\n\nACCOUNT ID:  " + str(self.account_id)
        text = text + "\nCustomer:  " + customers.get_name_by_id(self.customer_id)
        text = text + " \nAccount Type:  " + self.account_type
        text = text + "\nBalance:  $" + HelperFunctions.format_currency(self.balance)
        return text
