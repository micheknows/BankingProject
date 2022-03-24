from Menus import Menus
from UserInteractions import UserInteractions
from Employees import Employees

class Banking:

    @property
    def ui(self):
        return self._ui

    @ui.setter
    def ui(self, u):
        self._ui = u

    @property
    def menus(self):
        return self._menus

    @menus.setter
    def menus(self, menu):
        self._menus = menu

    def __init__(self):
        self.menus = Menus(self)
        self.menus.main_menu()
        self.ui = UserInteractions()
        self.emp = Employees()


    def display_menu(self):
        choice = self.ui.display_menu(self.menus)
        list(self.menus.menu_choices.values())[choice-1]()

    def employees(self):
        self.menus.menu_choices = self.emp.get_menu()
        self.add_suffixes()
        self.menus.menu_location = self.emp.get_menu_location()
        self.display_menu()

    def add_suffixes(self):
        self.menus.menu_choices['Return to Main Menu'] = self.return_main
        self.menus.menu_choices["Quit"] = self.menus.quit

    def show_menu(self):
        return self.menus.keep_going

    def return_main(self):
        self.menus.main_menu()
        self.display_menu()



b = Banking()
while b.show_menu():
    b.display_menu()
    if b.show_menu():
        input()
