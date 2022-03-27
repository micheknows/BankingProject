from Menus import Menus
from HelperFunctions import HelperFunctions
from Customers import Customers
from Accounts import Accounts
from Services import Services
from Employees import Employees


class Users:

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
        self.keep_going = True
        self.current_menu_items = []
        self.create_main_menu()
        self.customers = Customers()
        self.accounts = Accounts()
        self.services = Services()
        self.employees = Employees()

    def create_main_menu(self):
        self.current_menu_items = []
        menu = Menus("Main")
        self.add_item(menu,"Customer Application", self.customer_application)
        self.add_item(menu,"Employee Application", self.employee_application)
        self.add_quit(menu)
        self.current_menu = menu

    def employee_application(self):
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
        if len(self.customers.customers) > 0:
            self.customers.get_current_id()
            if self.customers.current_id > 0:
                self.current_menu_items = []
                menu = Menus("Customer")
                self.add_item(menu, "View My Profile", lambda:getattr(self.customers, "view_self")())
                self.add_item(menu, "View My Accounts", lambda:getattr(self.accounts, "view_customer_accounts")(self.customers.current_id))
                self.add_item(menu, "Make Account Transaction", lambda:getattr(self.accounts, "make_account_transaction")(self.customers.current_id))
                self.add_item(menu, "Apply For Loan", lambda:getattr(self.customers, "apply_service")("loan"))
                self.add_item(menu, "Apply For Credit Card", lambda:getattr(self.customers, "apply_service")("credit card"))
                self.add_item(menu, "View My Services", lambda:getattr(self.customers, "view_self_services")())
                self.add_return(menu)
                self.add_quit(menu)
                self.current_menu = menu
        else:
            print("We do not have any customers at this bank, yet.  Therefore, you are unable to login as a customer.")


    def add_item(self, menu, desc, func):
        menu.add_item(desc)
        self.current_menu_items.append(func)

    def add_quit(self, menu):
        menu.add_quit()
        self.current_menu_items.append(self.quit_function)

    def add_return(self, menu):
        menu.add_return()
        self.current_menu_items.append(self.return_function)

    def return_function(self):
        self.create_main_menu()

    def quit_function(self):
        self.keep_going = False

    def display_menu(self):
        print(self.current_menu)
        choice = int(input())
        self.current_menu_items[choice-1]()


u = Users()
while u.keep_going:
    u.display_menu()
