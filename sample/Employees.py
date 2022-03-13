
class Employees:

    def __init__(self, banking):
        self.banking = banking


    def get_application_menu(self):
        menu_choices  = {
            "Customer Management" : self.customer_management,
            "Services Management" : self.dummy_func,
            "Account Management" : self.account_management,
            "Return to Main Menu" : self.return_main,
            "Quit": self.quit
        }
        menu_name = "Employee Application"
        return [menu_choices, menu_name]

    def customer_management(self):
        self.banking.customer_manage()

    def account_management(self):
        self.banking.account_manage()

    def return_main(self):
        self.banking.location = "return"
        self.banking.main_menu()

    def quit(self):
        self.banking.location="quit"

    def dummy_func(self):
        pass

