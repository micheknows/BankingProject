from HelperFunctions import HelperFunctions
import logging


class Customer:
    """
    A class to represent a customer

    ...

    Attributes
    -----------
    id : int
        the identification for the customer
    first_name : str
        first name of the customer
    last_name : str
        last name of the customer
    address : str
        address of the customer

    Methods
    ---------
    __str__():
        returns a user-friendly string representation of the customer object

    """

    def __init__(self, id_list):
        """
        Constructs all the necessary attributes for the customer object

        Parameters
        -----------
            id_list : List(int)
                list of the ids associated with all customer objects

        """

        logging.basicConfig(filename="banking.log",
                            format='%(asctime)s %(message)s',
                            filemode='a')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.customer_id = HelperFunctions.get_next_id(id_list)
        self.first_name = HelperFunctions.get_string("Please enter the customer's first name:  ")
        self.last_name = HelperFunctions.get_string("Please enter the customer's last name:  ")
        self.address = HelperFunctions.get_string("Please enter the customer's address:  ")

    def __str__(self):
        """
        returns a user-friendly string representation of the customer

        Parameters
        -------------
        None

        Returns
        -------------
        text    :   str
            user-friendly string of the attributes of the customer object

        """
        text = "\n\n**********\n\nCUSTOMER ID:  " + str(self.customer_id)
        text = text + "\nName:  " + self.first_name + " " + self.last_name
        text = text + "\nAddress:  " + self.address
        return text
