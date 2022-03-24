class Employees:

    def get_menu(self):
        menu_choices = {"Create a Customer": self.dummy,
                         "Delete a Customer" : self.dummy
                        }
        return menu_choices

    def get_menu_location(self):
        return "Employee"

    def dummy(self):
        print('hi')