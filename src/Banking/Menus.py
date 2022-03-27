import logging


# noinspection PyIncorrectDocstring
class Menus:
    """
    A class to display menus for the user

    ...

    Attributes
    -----------
    name : str
        name of the menu
    items : List(str)
        items in the menu

    Methods
    ---------
    add_item(desc):
        adds an item to the menu

    add_return():
        adds a "Return to Main Menu" item

    add_quit():
        adds a "Quit" menu item

    __str__():
        returns a text representation of the current menu

    """

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    def __init__(self, name):
        """
        Constructs all the necessary attributes for the Menus object

        Parameters
        -----------
            name    :   str
                name of the menu
            items   :   List(str)
                list of the menu choices


        """

        logging.basicConfig(filename="banking.log",
                            format='%(asctime)s %(message)s',
                            filemode='a')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.name = name
        self.items = []

    def add_item(self, desc):
        """
        adds an item to the menu

        Parameters
        -------------
        desc    :   str
            description of the menu choice that will be displayed to the user

        Returns
        -------------
        None

        """
        self.items.append(desc)

    def add_return(self):
        """
        adds a "Return to Main Menu" item to the menu

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        self.items.append("Return to Main Menu")

    def add_quit(self):
        """
        adds a "Quit" item to the menu

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        self.items.append("Quit")

    def __str__(self):
        """
        returns a string representation of the current menu

        Parameters
        -------------
        None

        Returns
        -------------
        text    :   str
            string representation of the entire current menu

        """
        text = "\n\n\n" + self.name + " Menu\n\n"
        text += "Please make your choice by typing the number.\n\n"
        for idx, item in enumerate(self.items,1):
            text = text + str(idx) + ".  " + item + "\n"
        return text
