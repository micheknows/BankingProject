from HelperFunctions import HelperFunctions
import logging


# noinspection PyIncorrectDocstring
class Service:
    """
    A class to represent a service object

    ...

    Attributes
    -----------
    service_id  :   int
        identification for the service
    customer_id :   int
        identification for the customer associated with the service
    balance     :   float
        amount left to pay for this service
    customers   :   Customers
        the Customers instance
    approved    :   bool
        whether the customer application has been through the approval process
    denied      :   bool
        whether the application was denied

    Methods
    ---------
    deny_app():
        denies a customer application
    approval_message():
        adds an extra message to string representation if the account has either not been through the approval process
        or if it was denied

    """
    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, logger):
        self._logger = logger

    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        self._service_id = service_id

    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self._customer_id = customer_id

    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    def customers(self):
        return self._customers

    @customers.setter
    def customers(self, customers):
        self._customers = customers

    def approved(self):
        return self._approved

    @approved.setter
    def approved(self, approved):
        self._approved = approved

    def denied(self):
        return self._denied

    @denied.setter
    def denied(self, denied):
        self._denied = denied

    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, reason):
        self._reason = reason

    def __init__(self, service_id, customer_id, customers, balance):
        """
        Constructs all the necessary attributes for the Services object

        Parameters
        -----------
            service_id : int
                the identification for the service
            customer_id : int
                the id for the customer associated with the service
            customers : Customers
                the Customers instance
            balance : float
                amount left to pay on the service


        """

        logging.basicConfig(filename="banking.log",
                            format='%(asctime)s %(message)s',
                            filemode='a')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.service_id = service_id
        self.customer_id = customer_id
        self.balance = balance
        self.customers = customers
        self.approved = False
        self.denied = False
        self.reason = ""

    def deny_app(self, reason):
        """
        denies the customer application

        Parameters
        -------------
        reason  :   str
            reason given for the denial

        Returns
        -------------
        None

        """
        self.reason = reason
        self.balance = 0

    def approval_message(self):
        """
        returns messages if the service either has not been through the approval process or if it was denied

        Parameters
        -------------
        None

        Returns
        -------------
        text    :   str
            messages if the service either has not been through the approval process or if it was denied

        """
        text = ""
        if not self.approved:
            if not self.denied:
                text = "\n\nYOUR APPLICATION FOR THE FOLLOWING IS PROCESSING.  WE WILL INFORM YOU OF OUR CREDIT " \
                       "DECISION.\n\n "
            else:
                text = "\n\nWe are sorry to inform you that this application was denied.\n\n"
        return text


class Loan(Service):
    """
    A subclass of Service to represent Loan objects

    ...

    Attributes
    -----------
    purpose  :   str
        purpose for the loan
    orig_loan_amt :   float
        amount of the original loan

    Methods
    ---------
    deny():
        sets loan amount to 0 and calls the super().denied()
    __str__():
        returns a string representation of the Loan object

    """

    def purpose(self):
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        self._purpose = purpose

    def orig_loan_amount(self):
        return self._orig_loan_amount

    @orig_loan_amount.setter
    def orig_loan_amount(self, orig_loan_amount):
        self._orig_loan_amount = orig_loan_amount

    def __init__(self, service_id, customer_id, amount, customers, purpose):
        """
        Constructs all the necessary attributes for the Loans object

        Parameters
        -----------
            service_id : int
                the identification for the service
            customer_id : int
                the id for the customer associated with the service
            amount  :   float
                amount the customer is requesting
            customers : Customers
                the Customers instance
            purpose :   str
                purpose of this loan


        """
        super().__init__(service_id, customer_id, customers, amount)
        self.purpose = purpose
        self.orig_loan_amount = amount

    def deny(self, reason):
        """
        calls super().deny_app(reason) and sets the loan amount to 0

        Parameters
        -------------
        reason  :   str
            reason for the denial

        Returns
        -------------
        None

        """
        super().deny_app(reason)
        self.orig_loan_amount = 0

    def __str__(self):
        """
        returns string representation of the service

        Parameters
        -------------
        None

        Returns
        -------------
        text    :   str
            string representation of the service

        """
        text = super().approval_message()
        text = text + "\n\n**********\n\nLOAN ID:  " + str(self.service_id)
        text = text + "\nCustomer:  " + self.customers.get_name_by_id(self.customer_id)
        text = text + "\nPurpose:  " + self.purpose
        text = text + "\nOriginal Loan Amount:  $" + HelperFunctions.format_currency(self.orig_loan_amount)
        text = text + "\nBalance:  $" + HelperFunctions.format_currency(self.balance)
        return text


class CreditCard(Service):
    """
    A subclass of Service to represent CreditCard objects

    ...

    Attributes
    -----------
    limit  :   float
        amount of available credit if approved

    Methods
    ---------
    deny():
        sets limit to 0 and calls the super().denied()
    __str__():
        returns a string representation of the CreditCard object

    """

    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, limit):
        self._limit = limit

    def __init__(self, service_id, customer_id, amount, customers):
        """
        Constructs all the necessary attributes for the CreditCard object

        Parameters
        -----------
            service_id : int
                the identification for the service
            customer_id : int
                the id for the customer associated with the service
            amount  :   float
                credit limit requested by the customer
            customers : Customers
                the Customers instance


        """
        super().__init__(service_id, customer_id, customers, 0)
        self.limit = amount

    def deny(self, reason):
        """
        calls super().deny_app(reason) and sets the credit limit to 0

        Parameters
        -------------
        reason  :   str
            reason for denial

        Returns
        -------------
        None

        """
        super().deny_app(reason)
        self.limit = 0

    def __str__(self):
        """
        returns string representation of the CreditCard

        Parameters
        -------------
        None

        Returns
        -------------
        text    :   str
            string representation of the CreditCard

        """
        text = super().approval_message()
        text = text + "\n\n**********\n\nCREDIT CARD ID:  " + str(self.service_id)
        text = text + "\nCustomer:  " + self.customers.get_name_by_id(self.customer_id)
        text = text + "\nCredit Limit:  $" + HelperFunctions.format_currency(self.limit)
        text = text + "\nBalance:  $" + HelperFunctions.format_currency(self.balance)
        return text
