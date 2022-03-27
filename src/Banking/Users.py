from Menus import Menus
from HelperFunctions import HelperFunctions
from Customers import Customers
from Accounts import Accounts
from Services import Services
from Employees import Employees
import logging


# noinspection PyIncorrectDocstring
class Users:
    """
    A class to handle menu tasks for users

    ...

    Attributes
    -----------
    keep_going : bool
        if True the program does not end and displays the menu again
    current_menu : Menu
        the current menu object
    current_menu_items : List(function)
        a list of functions that match the menu descriptions
    customers   :   Customers()
        Customers instance
    accounts   :   Accounts()
        Accounts instance
    services   :   Services()
        Services instance
    employees   :   Employees()
        Employees instance

    Methods
    ---------
     create_main_menu():
        creates the main menu

    employee_application():
        creates the employee menu

    customer_application():
        creates the customer menu

    add_item(menu, desc, func):
        adds an item to menu

    add_quit(menu):
        adds 'Quit' to the menu

    add_return(menu):
        adds 'Return to Main Menu' to the menu

    return_function():
        resets to main menu when 'return to main menu' is chosen

    quit_function():
        ends the program

    display_menu():
        displays the current menu, gets user input and runs the associated method

    """

    @property
    def keep_going(self):
        return self._keep_going

    @keep_going.setter
    def keep_going(self, kg):
        self._keep_going = kg

    @property
    def current_menu(self):
        return self._current_menu

    @current_menu.setter
    def current_menu(self, cm):
        self._current_menu = cm

    @property
    def current_menu_items(self):
        return self._current_menu_items

    @current_menu_items.setter
    def current_menu_items(self, cmi):
        self._current_menu_items = cmi

    def __init__(self):
        """
        Constructs all the necessary attributes for the Users class

        Parameters
        -----------
            None


        """

        logging.basicConfig(filename="banking.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.keep_going = True
        self.current_menu = None
        self.current_menu_items = []
        self.create_main_menu()
        self.customers = Customers()
        self.accounts = Accounts()
        self.services = Services()
        self.employees = Employees()

    def create_main_menu(self):
        """
        creates the main menu

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        self.current_menu_items = []
        menu = Menus("Main")
        self.add_item(menu,"Customer Application", self.customer_application)
        self.add_item(menu,"Employee Application", self.employee_application)
        self.add_quit(menu)
        self.current_menu = menu

    def employee_application(self):
        """
        creates the employee menu

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        self.current_menu_items = []
        menu = Menus("Employee")
        self.add_item(menu, "Create a Customer", lambda:getattr(self.customers, "create_customer")())
        self.add_item(menu, "View All Customers", lambda:getattr(self.employees, "view_all_customers")())
        self.add_item(menu, "Delete A Customer", lambda:getattr(self.customers, "delete_customer")())
        self.add_item(menu, "Create an Account", lambda:getattr(self.employees, "create_account")())
        self.add_item(menu,"Add Fee to Account", lambda:getattr(self.employees, "add_account_fee")())
        self.add_item(menu,"Approve Services", lambda:getattr(self.employees, "approve_services")())
        self.add_return(menu)
        self.add_quit(menu)
        self.current_menu = menu

    def customer_application(self):
        """
        creates the customer menu

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        if len(self.customers.customers) > 0:
            self.customers.get_current_id()
            if self.customers.current_id > 0:
                self.current_menu_items = []
                menu = Menus("Customer")
                self.add_item(menu, "View My Profile",
                              lambda:getattr(self.customers, "view_self")())
                self.add_item(menu, "View My Accounts",
                              lambda:getattr(self.accounts, "view_customer_accounts")(self.customers.current_id))
                self.add_item(menu, "Make Account Transaction",
                              lambda:getattr(self.accounts, "make_account_transaction")(self.customers.current_id))
                self.add_item(menu, "Apply For Loan",
                              lambda:getattr(self.services, "apply_service")("loan", self.customers.current_id))
                self.add_item(menu, "Apply For Credit Card",
                              lambda:getattr(self.services, "apply_service")("credit card", self.customers.current_id))
                self.add_item(menu, "View My Services",
                              lambda:getattr(self.customers, "view_self_services")(self.customers.current_id))
                self.add_return(menu)
                self.add_quit(menu)
                self.current_menu = menu
        else:
            self.logger.warning("No customers were available.  Does data exist?")
            print("We do not have any customers at this bank, yet.  Therefore, you are unable to login as a customer.")

    def add_item(self, menu, desc, func):
        # noinspection GrazieInspection
        """
                adds an item to the current menu

                Parameters
                -------------
                menu    :   Menu
                    current Menu object
                desc    :   str
                    description that will be displayed to the user in the menu
                func    :   function
                    function that will run for this menu choice

                Returns
                -------------
                None

                """
        menu.add_item(desc)
        self.current_menu_items.append(func)

    def add_quit(self, menu):
        """
        adds 'Quit' to the current menu

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        menu.add_quit()
        self.current_menu_items.append(self.quit_function)

    def add_return(self, menu):
        """
        adds 'Return to the Main Menu' to the current menu

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        menu.add_return()
        self.current_menu_items.append(self.return_function)

    def return_function(self):
        """
        resets to main menu when 'return to main menu' is chosen

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        self.create_main_menu()

    def quit_function(self):
        """
        sets keep_going False to end the program

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        self.keep_going = False

    def display_menu(self):
        """
        displays the current menu, gets user choice input and runs the associated function

        Parameters
        -------------
        None

        Returns
        -------------
        None

        """
        print(self.current_menu)
        choice = int(input())
        self.current_menu_items[choice-1]()


u = Users()
while u.keep_going:
    u.display_menu()
