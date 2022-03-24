class Menus:

    @property
    def menu_choices(self):
        return self._menu_choices

    @menu_choices.setter
    def menu_choices(self, mc):
        self._menu_choices = mc

    @property
    def menu_location(self):
        return self._menu_location

    @menu_location.setter
    def menu_location(self, ml):
        self._menu_location = ml

    def __init__(self, banking):
        self.keep_going = True
        self.banking = banking



    def main_menu(self):
        self.menu_choices = {"Customer Application" : self.dummy, "Employee Application" : self.banking.employees}
        self.menu_location = "Main"
        self.add_quit()

    def add_quit(self):
        self.menu_choices["Quit"] = self.quit

    def quit(self):
        self.keep_going = False


    def dummy(self):
        pass


    def __str__(self):
        text = "\n" + self.menu_location + " Menu"
        text += "\nMake your selection by number:\n\n"
        for index, choice in enumerate(self.menu_choices.keys(),1):
            text += str(index)
            text += ".  "
            text += choice
            text += "\n"
        return text


