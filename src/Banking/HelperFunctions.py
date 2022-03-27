import logging


class HelperFunctions:
    """
    A class to provide helper functions

    ...

    Attributes
    -----------
    None

    Methods
    ---------
    get_string(prompt):
        returns string input from user with no validation

    get_integer(prompt):
        returns valid integer input from user

    get_float(prompt):
        returns valid float input from user

    get_next_id(id_list):
        gets the next valid id from any list of objects with id attribute

    format_currency(num):
        returns a float with 2 decimal places for currency

    get_valid_id(id_list, prompt):
        returns a valid id from user input that is not in the list of already used ids

    get_string_from_list(string_list, prompt):
        returns a valid str from user input that is contained within the list of accepted strings

    """

    def __init__(self):
        logging.basicConfig(filename="banking.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

    @staticmethod
    def get_string(prompt):
        """
        returns a string from user input

        Parameters
        -------------
        prompt  :   str
            the text that will be displayed to the user to ask for input

        Returns
        -------------
        text    :   str
            string the user input

        """
        print(prompt)
        return input()

    @staticmethod
    def get_integer(prompt):
        """
        returns a valid integer from user input

        Parameters
        -------------
        prompt  :   str
            the text that will be displayed to the user to ask for input

        Returns
        -------------
        number    :   int
            user input formatted to a valid integer

        """
        print(prompt)
        while True:
            try:
                num = int(input())
                return num
            except ValueError:
                print("Please try again.  The entry must be an integer.")

    @staticmethod
    def get_float(prompt):
        """
        returns a valid float from user input

        Parameters
        -------------
        prompt  :   str
            the text that will be displayed to the user to ask for input

        Returns
        -------------
        number    :   int
            user input formatted to a valid float

        """
        print(prompt)
        while True:
            try:
                num = float(input())
                return num
            except ValueError:
                print("Please try again.  The entry must be a decimal.")

    @staticmethod
    def get_next_id(id_list):
        """
        returns the next valid id for a list of objects

        Parameters
        -------------
        id_list  :   List(objects)
            list of objects with an id attribute

        Returns
        -------------
        next_id    :   int
            the next available id for the list of objects

        """
        next_id = 1
        for used_id in id_list:
            if used_id >= next_id:
                next_id = used_id+1
        return next_id

    @staticmethod
    def format_currency(num):
        """
        returns a string formatted for currency

        Parameters
        -------------
        num  :   float
            the number to be formatted

        Returns
        -------------
        number    :   str
            the original number formatted to a string to represent currency

        """
        return "{:.2f}".format(num)

    @staticmethod
    def get_valid_id(id_list, prompt):
        """
        returns a valid id from user input that is not in the list of already used ids

        Parameters
        -------------
        id_list :   List(int)
            list of ids that are already in use
        prompt  :   str
            the text that will be displayed to the user to ask for input

        Returns
        -------------
        valid_id    :   int
            next available valid id

        """
        print(prompt)
        valid_id = int(input())
        while valid_id not in id_list and valid_id != 0:
            print("That is not a valid id.  \n" + prompt + "\nOr, enter 0 to cancel and return to the menu.")
            valid_id = int(input())
        return valid_id

    @staticmethod
    def get_string_from_list(string_list, prompt):
        """
        returns a valid string from user input that is in the list of acceptable strings

        Parameters
        -------------
        string_list :   List(str)
            list of strings that are accepted
        prompt  :   str
            the text that will be displayed to the user to ask for input

        Returns
        -------------
        msg    :   str
            valid user input

        """
        print(prompt)
        msg = input()
        while msg.lower() not in string_list and msg != "@":
            print("That is not a valid entry.  \n" + prompt + "\nOr, enter @ to cancel and return to the menu.")
            msg = input()
        return msg
