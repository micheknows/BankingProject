
class Menus:

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, desc):
        self.items.append(desc)

    def add_return(self):
        self.items.append("Return to Main Menu")

    def add_quit(self):
        self.items.append("Quit")

    def __str__(self):
        text = "\n\n\n" + self.name + " Menu\n\n"
        text += "Please make your choice by typing the number.\n\n"
        for idx, item in enumerate(self.items,1):
            text = text + str(idx) + ".  " + item + "\n"
        return text
