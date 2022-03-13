
class Employees:

    def __init__(self, banking):
        self.banking = banking


    def get_application_menu(self):
        menu_choices  = {
            "Customer Management" : self.customer_management,
            "Services Management" : self.dummy_func,
            "Account Management" : self.dummy_func,
            "Return to Main Menu" : self.return_main,
            "Quit": self.quit
        }
        menu_name = "Employee Application"
        return [menu_choices, menu_name]

    def customer_management(self):
        self.banking.customer_manage()

    def return_main(self):
        self.banking.location = "return"
        self.banking.previous_menu()

    def quit(self):
        self.banking.location="quit"

    def dummy_func(self):
        pass



#
#     def __init__(self):
#         self.quit_now = False
#         self.return_now = False
#       #  self.customers = Customers()
#
#
#         self.menu_choices = {
#             "Customer Management" : self.show_customer_management,
#             "Services Application" : self.show_services_application,
#             "Return to Main Menu" : self.return_main,
#             "Quit": self.quit
#         }
#         self.menu = Menus(list(self.menu_choices.keys()),"Main")
#
#     def show_menu(self, menutype=""):
#         self.menu_choices[self.menu.display_menu()]()
#
#    # def show_customer_management(self):
#       #  self.customers.show_menu("management")
#
#     def show_services_application(self):
#         pass
#
#
#     def quit(self):
#         self.quit_now = True
#
#     def return_main(self):
#         self.return_now = True
#         self.currentID = -1
