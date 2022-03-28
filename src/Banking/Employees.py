from HelperFunctions import HelperFunctions
from Services import Services
from Customers import Customers
from Accounts import Accounts
from Data import Data
import logging


# noinspection PyIncorrectDocstring
class Employees:
    """
    A class to handle tasks that can be done by Employees

    ...

    Attributes
    -----------
    None

    Methods
    ---------
    view_all_customers():
        displays list of all customer objects

    create_account():
        creates a new account

    add_account_fee():
        adds a fee to an account

    approve_services():
        approve or deny services for which customers have applied

    """
    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, logger):
        self._logger = logger

    def __init__(self):
        logging.basicConfig(filename="banking.log",
                            format='%(asctime)s %(message)s',
                            filemode='a')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

    # noinspection PyMethodMayBeStatic
    def view_all_customers(self):
        """
        displays a list of all customer objects

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        customers = Customers()
        customers.view_customer_list()

    # noinspection PyMethodMayBeStatic
    def create_account(self):
        """
        creates a new account object

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        accounts = Accounts()
        accounts.create_account()

    # noinspection PyMethodMayBeStatic
    def add_account_fee(self):
        """
        adds a fee to an account

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        accounts = Accounts()
        accounts.add_fee()

    # noinspection PyMethodMayBeStatic
    def approve_services(self):
        """
        approve or deny services for which customers have applied

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        services = Services(Customers())
        waiting_list = [service for service in services.services if not service.approved and not service.denied]
        print("\n\nThere are " + str(len(waiting_list)) + " services waiting for a credit decision.\n\n")
        for item in services.services:
            if item in waiting_list:
                print(str(item))
                approve = HelperFunctions.get_string_from_list(["a", "d", "w"], "Please enter a to approve or d to "
                                                               "deny this application (or  w to wait)")
                if approve == "a":
                    item.approve_app()
                    Data.save_data(services.services, "services")
                elif approve == "d":
                    reason = HelperFunctions.get_string("What is the denial reason?")
                    item.deny(reason)
                    Data.save_data(services.services, "services")
