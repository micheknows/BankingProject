from Account import Account
from Data import Data
from HelperFunctions import HelperFunctions
import logging


class AccountsList:
    """
    A class to process a list of Accounts for viewing

    ...

    Attributes
    -----------
    list : List(Account)
        list of Account objects

    Methods
    ---------
    __str__():
        returns a user-friendly string representation of the list of Account objects in brief format

    """

    def __init__(self, accounts=()):
        """
        Constructs all the necessary attributes for the AccountsList object

        If the argument 'accounts' is not passed, the saved account data for all accounts is loaded

        Parameters
        -----------
            accounts    : List(Account), optional
                list of accounts

        """

        logging.basicConfig(filename="banking.log",
                            format='%(asctime)s %(message)s',
                            filemode='a')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        if len(accounts) < 1:
            self.list = Data.retrieve_data("accounts")
        else:
            self.list = accounts

    def __str__(self):
        """
        returns a user-friendly string representation of the list of accounts in brief format

        Parameters
        -------------
        None

        Returns
        -------------
        text    :   str
            user-friendly string of the attributes of the account objects in a one-object-per-row list

        """
        text = ""
        for account in self.list:
            id_section = "\nAccount ID:  " + str(account.id)
            name_section = "Customer:  " + account.customers.get_name_by_id(account.customer_id)
            balance_section = "Balance:  $" + HelperFunctions.format_currency(account.balance)
            text = text + '{:<25} {:<60} {}'.format(id_section, name_section, balance_section)
        return text
