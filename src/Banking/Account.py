from Customers import Customers
from HelperFunctions import HelperFunctions
import logging


# noinspection PyUnresolvedReferences
class Account:
    """
    A class to represent an account

    ...

    Attributes
    -----------
    account_id : int
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

        logging.basicConfig(filename="banking.log",
                            format='%(asctime)s %(message)s',
                            filemode='a')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
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
        try:
            text = text + "\nCustomer:  " + customers.get_name_by_id(self.customer_id)
        except IndexError:
            text = text + "\nERROR:  THIS ACCOUNT IS NOT ASSOCIATED WITH A VALID CUSTOMER"
            self.logger.error("Account id " + str(self.account_id) + " is associated with customer id " +
                              str(self.customer_id) + " which is not a valid customer id.")

        text = text + " \nAccount Type:  " + self.account_type
        text = text + "\nBalance:  $" + HelperFunctions.format_currency(self.balance)
        return text
