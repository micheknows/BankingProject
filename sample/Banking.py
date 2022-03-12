from Menus import Menus
from Customers import Customers

class Banking:
    def __init__(self):
        self.quit_now = False
        self.return_now = False
        self.menu_choices = {
            "Customer Application" : self.show_customer_application,
            "Employee Application" : self.show_employee_application,
            "Quit": self.quit
        }
        self.menu = Menus(list(self.menu_choices.keys()),"Main")

    def show_menu(self):
        self.menu_choices[self.menu.display_menu()]()

    def show_customer_application(self):
        customer = Customers()
        self.show_application(customer)

    def show_application(self, application):
        while application.quit_now==False:
            application.show_menu()
            if application.return_now or application.quit_now:
                self.return_now = True
                if application.quit_now:
                    self.quit_now = True
                break
            else:
                if application.quit_now==False and application.return_now==False:
                    print("Press Enter to return to current menu")
                    input()

    def show_employee_application(self):
        print("You asked for the employee applicaton")


    def quit(self):
        self.quit_now = True


banking = Banking()
while True:
    banking.show_menu()
    if banking.quit_now:
        break
    else:
        if not banking.return_now:
            print("Press Enter to return to current menu")
            input()
        else:
            banking.return_now = False
