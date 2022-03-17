from CustomerFunctions import CustomerFunctions
from EmployeesFunctions import EmployeesFunctions

class UserFunctions:

    def __init__(self):
        self.cf = CustomerFunctions()
        self.ef = EmployeesFunctions()
        self.exit = False
        self.location = "Main"
        self.main_menu_choices = {
            "Customer Application" : self.show_customer_application,
            "Employee Application" : self.show_employee_application
        }
        self.menu_return = {
            "Return to Main Menu" : self.return_menu
        }
        self.menu_quit = {
            "Quit" : self.quit_menu
        }
        self.main_location = "Main"
        self.choices = self.main_menu_choices
        self.location = self.location
        self.show_menu()



    def show_menu(self):
        choices = self.choices
        print(self.location + " Menu")
        if self.location != "Main":
            choices = {**choices, **self.menu_return}
        choices = {**choices, **self.menu_quit}
        for index, key in enumerate(choices.keys(),1):
            print(str(index) + ".  " + key)
        while True:
            print("Enter your choice:")
            try:
                choice = int(input())
                if choice > 0 and choice < len(choices)+1:
                    break
            except:
                print("You must enter one of the listed choices as a number")
        list(choices.values())[choice-1]()

    def quit_menu(self):
        self.exit=True

    def return_menu(self):
        self.cf.currentID = None
        self.ef.currentID = None
        self.choices, self.location = self.main_menu_choices, self.main_location
        self.show_menu()

    def show_customer_application(self):
        self.choices, self.location = self.cf.customer_application_menu()
        self.show_menu()

    def show_employee_application(self):
        self.choices, self.location = self.ef.employee_application_menu()
        self.show_menu()

uf = UserFunctions()
while uf.exit == False:
    uf.show_menu()
