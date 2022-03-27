from HelperFunctions import HelperFunctions
from Customer import Customer
from Data import Data
from Services import Services
import logging


# noinspection PyIncorrectDocstring
class Customers:
    """
    A class to handle tasks associated with customers

    ...

    Attributes
    -----------
    customers : List(Customer)
        list of all customer objects

    current_id  :   int
        id of the current customer using the system

    Methods
    ---------
    create_customer():
        creates a new customer object

    get_name_by_id(customer_id):
        returns properly formatted customer full name

    get_current_id():
        gets a valid customer id from user input

    view_self():
        displays customer object for the current customer

    view_customer_list(clist=()):
        displays a user-friendly list of all customer objects

    brief_list(clist):
        displays a one-customer-per-row brief list of all customer objects

    delete_customer():
        gets a valid customer id from user input then processes customer deletion

    delete_customer_by_id(customer_id):
        returns a list of customers after deleting a customer by customer id

    get_customer_by_id(id):
        returns a customer object that matches a particular customer id

    save():
        saves all customer objects to file


    """

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, logger):
        self._logger = logger

    @property
    def customers(self):
        return self._customers

    @customers.setter
    def customers(self, customers):
        self._customers = customers

    @property
    def current_id(self):
        return self._current_id

    @current_id.setter
    def current_id(self, current_id):
        self._current_id = current_id

    def __init__(self):
        """
        Constructs all the necessary attributes for the Customers object

        Parameters
        -----------
            None


        """

        logging.basicConfig(filename="banking.log",
                            format='%(asctime)s %(message)s',
                            filemode='a')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.customers = Data.retrieve_data("customers")
        self.current_id = None

    def create_customer(self):
        """
        creates a new customer object

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        self.customers.append(Customer([customer.customer_id for customer in self.customers]))
        print("Customer created")
        print(self.customers[len(self.customers)-1])
        self.save()

    def get_name_by_id(self, customer_id):
        """
        returns the properly formatted customer full name for the customer id

        Parameters
        -------------
        customer_id :   int
            id of the customer

        Returns
        -------------
        text    :   str
            properly formatted full name of customer object

        """
        customer_name = [c.first_name + " " + c.last_name for c in self.customers if c.customer_id == customer_id]
        if len(customer_name) > 0:
            return customer_name[0]
        else:
            return ""

    def get_current_id(self):
        """
        assigns valid customer id to the current_id for the Customers class

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        self.current_id = HelperFunctions.get_valid_id([c.customer_id for c in self.customers], "Enter your customer "
                                                                                                "id:  ")

    def view_self(self):
        """
        prints a user-friendly string representation of the customer object for the current customer id

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        print(self.get_customer_by_id(self.current_id))

    def view_customer_list(self, clist=()):
        """
        prints a user-friendly list of all customer objects

        If the argument 'clist' is not passed, then the list of all saved customer objects is loaded and used

        Parameters
        -------------
        clist   :   List(Customer), optional
            list of customer objects to be printed, default = empty list

        Returns
        -------------
        None

        """
        if len(clist) < 1:
            clist = Data.retrieve_data("customers")
        if len(clist) > 0:
            print(self.brief_list(clist=clist))
        else:
            print("There are no customers to view.")

    # noinspection PyMethodMayBeStatic
    def brief_list(self, clist):
        """
        returns a user-friendly string representation of the list of customer objects in brief one-customer-per-row
        format

        Parameters
        -------------
        clist   :   List(Customer)
            list of customer objects to return

        Returns
        -------------
        text    :   str
            user-friendly string representation of the list of customer objects in brief one-customer-per-row format

        """
        text = ""
        for customer in clist:
            id_section = "\nCustomer ID:  " + str(customer.customer_id)
            name_section = "Name:  " + customer.first_name + " " + customer.last_name
            address_section = "Address:  " + customer.address
            text = text + '{:<25} {:<60} {}'.format(id_section, name_section, address_section)
        return text

    def delete_customer(self):
        """
        determines customer to delete from user input then passes to deletion

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        self.view_customer_list()
        c_id = HelperFunctions.get_valid_id([c.customer_id for c in self.customers], "\nEnter the customer id of the "
                                                                                     "customer you "
                                                                                     "wish to delete:  ")
        if c_id == 0:
            print("No valid customer to delete")
        else:
            print("Customer deleted")
            self.customers = self.delete_customer_by_id(c_id)
            self.save()

    def delete_customer_by_id(self, customer_id):
        """
        returns list of customer objects after deleting customer based on customer id

        Parameters
        -------------
        customer_id     :   int
            customer id to be deleted

        Returns
        -------------
        customers_list  :   List(Customer)
            list of customer objects after customer object with customer_id was deleted

        """
        return [c for c in self.customers if c.customer_id != customer_id]

    # noinspection GrazieInspection
    def get_customer_by_id(self, customer_id):
        """
        returns customer object that matches customer_id

        Parameters
        -------------
        customer_id     :   int
            customer id

        Returns
        -------------
        customer    :   Customer
            customer object that matches customer id

        """
        try:
            return [c for c in self.customers if c.customer_id == customer_id][0]
        except IndexError:
            return None

    def save(self):
        """
        saves all customer objects to file

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        Data.save_data(self.customers, "customers")
