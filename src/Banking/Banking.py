from Menus import Menus

class Banking:

    def __init__(self):
        self.do_main_menu()
        self.quit = False

    def show_menu(self):
        print(Menus.build_menu(self.menu_choices, self.menu_location))
        choice = int(input())
        list(self.menu_choices.values())[choice-1]()

    def emp_menu(self):
        self.menu_choices = {
                                "Create a Customer" : self.create_customer,
                                "Delete a Customer" : self.delete_customer,
                                "Return to Main Menu" : self.do_main_menu,
                                "Quit" : self.quit_now
                            }
        self.menu_location = "Employee"

    def create_customer(self):
        pass

    def delete_customer(self):
        pass


    def do_main_menu(self):
        self.menu_choices = {
                    "Customer Application" : self.dummy,
                    "Employee Applicaiton" : self.emp_menu,
                    "Quit" : self.quit_now
                    }
        self.menu_location = "Main"

    def quit_now(self):
        self.quit = True


    def dummy(self):
        pass


b = Banking()
while not b.quit:
    b.show_menu()
    if b.quit:
        break