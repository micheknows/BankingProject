from HelperFunctions import HelperFunctions
from Account import Account
from Data import Data
from Customers import Customers
from AccountsList import AccountsList
import logging


# noinspection PyIncorrectDocstring
class Accounts:
    """
    A class to handle tasks associated with accounts

    ...

    Attributes
    -----------
    accounts : List[Account]
        list of all account objects
    account_types : List[str]
        the types of accounts that are available (i.e.  checking, savings)


    Methods
    ---------
    get_valid(valid):
        decorator that determines if a method needs a valid customer and/or a valid account from user input

    get_valid_account_by_customer_id(customer_id):
        gets a valid account id for a particular customer id from user input

    view_customer_accounts(customer_id):
        displays a list of accounts that belong to a particular customer

    get_valid_customer():
        gets a valid customer id from user input

    create_account(customer_id="")
        creates an account for a customer

    add_fee(customer_id="", account_id="")
        adds an account fee

    transaction(account_id, amt):
        processes deposit or withdrawal for customer's account

    make_account_transaction(customer_id):
        determines the type and amount of transaction for a customer's account

    get_account_by_id(account_id):
        returns an account object associated with a particular account id

    get_account_list_by_customer_id(customer_id):
        returns a list of account objects that are associated with a particular customer id

    view_account_list(account_list):
        displays a list of accounts

    save():
        saves the list of account objects

    """

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, logger):
        self._logger = logger

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts

    @property
    def account_types(self):
        return self._account_types

    @account_types.setter
    def account_types(self, account_types):
        self._account_types = account_types

    def __init__(self):
        """
        Constructs all the necessary attributes for the Accounts object

        Parameters
        -----------
            accounts : List(Account)
                list of all account objects
            account_types : List(str)
                list of valid account types (i.e. checking, savings)


        """

        logging.basicConfig(filename="banking.log",
                            format='%(asctime)s %(message)s',
                            filemode='a')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.accounts = Data.retrieve_data("accounts")
        self.account_types = ["checking", "savings"]

    def get_valid(valid):
        """
        determines if decorated function requires a valid customer and/or account id

        Parameters
        -------------
        valid       :       (List(str))
            list of which valid ids are required

        Returns
        -------------
        fn          :       function
            returns valid customer id and/or valid account id to decorated function

        """
        def decorator(fn):
            def decorated(*args, **kwargs):
                if 'customer' in valid:
                    customer_id = Accounts.get_valid_customer()
                    if customer_id > 0:
                        if 'account' in valid:
                            account_id = Accounts.get_valid_account_by_customer_id(customer_id)
                            if account_id > 0:
                                fn(customer_id=customer_id, account_id=account_id, *args, **kwargs)
                        else:
                            fn(customer_id=customer_id, *args, **kwargs)
            return decorated
        return decorator

    def get_valid_account_by_customer_id(customer_id):
        """
        returns a valid account id from user input

        Parameters
        -------------
        customer_id     :   int
            id of the customer

        Returns
        -------------
        account_id      :   int
            id of the valid account associated with the customer

        """
        accounts = Data.retrieve_data("accounts")
        aid_list = [a.id for a in accounts if a.customer_id == customer_id]
        if len(Accounts.get_account_list_by_customer_id(Accounts(), customer_id)) < 1:
            print("There are no valid accounts for this customer.")
            return 0
        else:
            print("Here are the customer's accounts:")
            print(AccountsList(accounts=Accounts.get_account_list_by_customer_id(Accounts(),customer_id)))
            account_id = HelperFunctions.get_valid_id(aid_list, "Enter the id for the customer's account:  ")
            return account_id

    def view_customer_accounts(self, customer_id):
        """
        displays a user-friendly list of accounts associated with a particular customer

        Parameters
        -------------
        customer_id     :   int
            id of the customer

        Returns
        -------------
        None

        """
        self.view_account_list(self.get_account_list_by_customer_id(customer_id))

    def get_valid_customer():
        """
        returns a valid customer id from user input

        Parameters
        -------------
        None

        Returns
        -------------
        customer_id    :    int
            valid id of the customer

        """
        customers = Customers()
        cid_list = [c.customer_id for c in customers.customers]
        if len(customers.customers) < 1:
            print("There are no valid customers at this bank.")
            logging.basicConfig(filename="banking.log",
                            format='%(asctime)s %(message)s',
                            filemode='a')
            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)
            logger.warning("No customers are loaded.  Does data exist?")
            return 0
        else:
            print("Here are the active customers:")
            print(customers.brief_list(customers.customers))
            customer_id = HelperFunctions.get_valid_id(cid_list, "\nEnter the customer id for the account:  ")
            return customer_id

    # noinspection PyArgumentList
    @get_valid(['customer'])
    def create_account(self, customer_id=""):
        """
        creates a new account

        Parameters
        -------------
        customer_id     :   int, optional
            default is none because this parameter is not passed with the function is called.  It is retrieved by
            the decorator

        Returns
        -------------
        None

        """
        account_id = HelperFunctions.get_next_id([account.id for account in self.accounts])
        account_type = HelperFunctions.get_string_from_list([s[0] for s in self.account_types],"Enter the first "
                                                                                               "letter of the account"
                                                                                               " type " + repr(
            self.account_types) + ":  ")
        if account_type != "@":
            balance = HelperFunctions.get_float("What is the opening deposit amount:  ")
            type_of_account = [s for s in self.account_types if s.startswith(account_type.lower())][0]
            self.accounts.append(Account(account_id, customer_id, type_of_account,balance))
            print("Account created")
            print(self.accounts[len(self.accounts)-1])
            self.save()

    # noinspection PyArgumentList,PyUnusedLocal
    @get_valid(['customer', 'account'])
    def add_fee(self, customer_id="", account_id=""):
        """
        adds a fee to a customer's account

        Parameters
        -------------
        customer_id     :   int, optional
            default is none because this parameter is not passed with the function is called.  It is retrieved by
            the decorator
        account_id     :   int, optional
            default is none because this parameter is not passed with the function is called.  It is retrieved by
            the decorator

        Returns
        -------------
        None

        """
        desc = HelperFunctions.get_string("What is the fee for?")
        amt = HelperFunctions.get_float("How much is the fee?")
        print(str(self.get_account_by_id(account_id)))
        print("\n\nFee Assessed for:  " + desc)
        print("\nFee Amount:  " + HelperFunctions.format_currency(amt))
        print("\nPrevious Balance:  " + HelperFunctions.format_currency(self.get_account_by_id(account_id).balance))
        self.get_account_by_id(account_id).balance = self.get_account_by_id(account_id).balance - amt
        print("\nCurrent Balance:  " + HelperFunctions.format_currency(self.get_account_by_id(account_id).balance))

    def transaction(self, account_id, amt):
        """
        processes a deposit or withdrawal on an account

        Parameters
        -------------
        account_id     :   int
            id of the account

        amt             :   float
            amount of the transaction (negative if a withdrawal)

        Returns
        -------------
        None

        """
        try:
            self.get_account_by_id(account_id).balance = self.get_account_by_id(account_id).balance + amt
            self.save()
        except AttributeError:
            self.logger.error("User tried to do a transaction for the account id " + str(account_id))
            print("That account id is invalid.")

    def make_account_transaction(self, customer_id):
        """
        gets user input for details of a deposit or withdrawal for an account

        Parameters
        -------------
        customer_id     :   int
            id of the customer

        Returns
        -------------
        None

        """
        transaction_types = ["deposit", "withdraw"]
        print("Here are your active accounts:")
        self.view_account_list(self.get_account_list_by_customer_id(customer_id))
        id_list = [a.id for a in self.accounts if a.customer_id == customer_id]
        account_id = HelperFunctions.get_valid_id(id_list, "Enter the account id:  ")
        if account_id > 0:
            transaction_type = HelperFunctions.get_string_from_list([s[0] for s in transaction_types],"Enter the "
                                                                                                      "first letter "
                                                                                                      "of the "
                                                                                                      "transaction "
                                                                                                      "type " + repr(
                transaction_types) + ":  ")
            if transaction_type != "@":
                amt = HelperFunctions.get_float("For how much?")
                if transaction_type == "w":
                    amt = amt * -1
                previous_balance = self.get_account_by_id(account_id).balance
                self.transaction(account_id, amt)
                t_list = [t for t in transaction_types if t.startswith(transaction_type.lower())][0].capitalize()
                print(t_list + "successful in the amount of $" + HelperFunctions.format_currency(amt))
                print("Previous balance:  $" + HelperFunctions.format_currency(previous_balance))
                print("New balance:  $" + HelperFunctions.format_currency(self.get_account_by_id(account_id).balance))

    def get_account_by_id(self, account_id):
        """
        returns an Account object that matches the account_id

        Parameters
        -------------
        account_id     :   int
            id of the account

        Returns
        -------------
        account      :   Account
            the account object that matches the account id

        """
        try:
            return [a for a in self.accounts if a.id == account_id][0]
        except IndexError:
            return 0

    def get_account_list_by_customer_id(self, customer_id):
        """
        returns a list of accounts that match a customer's id

        Parameters
        -------------
        customer_id     :   int
            id of the customer

        Returns
        -------------
        accounts      :   List(Account)
            list of accounts that match the customer id

        """
        return [account for account in self.accounts if account.customer_id == customer_id]

    # noinspection PyMethodMayBeStatic
    def view_account_list(self, account_list):
        """
        displays a list of accounts in a brief user-friendly format

        Parameters
        -------------
        account_list     :   List(Account)
            list of accounts

        Returns
        -------------
        None

        """
        if len(account_list) > 0:
            print(AccountsList(accounts=account_list))
        else:
            print("No accounts for this customer.")

    def save(self):
        """
        saves account objects to a file

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        Data.save_data(self.accounts, "accounts")
