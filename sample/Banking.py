from Menus import Menus
from Customers import Customers
from Employees import Employees

class Banking:

    def __init__(self):
        self.location = "banking"
        self.create_default_menu()
        self.customers = Customers(self)
        self.employees = Employees(self)

    def create_default_menu(self):
        self.menu_choices = {
            "Customer Application" : self.customer_app,
            "Employee Application" : self.employee_app,
            "Quit" : self.quit
        }
        self.menu_name = "Main"

    def customer_app(self):
        choices, name = self.customers.get_application_menu()
        self.get_menu_values(choices, name, "customer_application")

    def customer_manage(self):
        choices, name = self.customers.get_manage_menu()
        self.get_menu_values(choices, name, "manage_customers")

    def employee_app(self):
        choices, name = self.employees.get_application_menu()
        self.get_menu_values(choices, name, "employee_application")

    def get_menu_values(self,choices, name, location):
        self.prev_menu_choices, self.prev_menu_name, self.prev_location = [self.menu_choices, self.menu_name, self.location]
        self.menu_choices, self.menu_name = choices, name
        self.location = location
        self.send_menu()

    def send_menu(self):
        self.menu = Menus(list(self.menu_choices.keys()), self.menu_name)
        self.menu_choices[self.menu.display_menu()]()



    def quit(self):
        self.location = "quit"

    def previous_menu(self):
        self.clear_screen()
        self.menu_choices, self.menu_name, self.location = [self.prev_menu_choices, self.prev_menu_name, self.prev_location]
        self.send_menu()

    def clear_screen(self):
        for x in range(20):
            print("")



banking = Banking()
while banking.location!="quit":
    banking.send_menu()



