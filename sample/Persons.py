from Menus import Menus



class Persons:

    def __init__(self, menu_choices, menu_name):
        self.menu_choices = menu_choices
        self.menu = Menus(list(menu_choices.keys()),menu_name)

    def show_menu(self):
        self.menu_choices[self.menu.display_menu()]()

    def add_person(self):
        print("What is the first name?")
        first_name = input()
        print("What is the last name")
        last_name = input()
        return first_name, last_name

    def ask_property(self, prop):
        print("Enter the " + prop + ":  ")
        return input()

    def sure(self):
        print("Are you sure? (Enter Y for yes)")
        if input()=="Y":
            return True
        else:
            return False

    def get_next_id(self, mylist):
        id = 0
        for item in mylist:
            if item.id > id:
                id = item.id
        return (id + 1)

    def get_by_id(self,mylist, id):
        for index, item in enumerate(mylist):
            if item.id==id:
                return index

    def ask_id(self):
        print("Enter the ID:  ")
        id = int(input())
        return id

    def display_one(self, item):
        print("***********************************************************")
        print(item)
        print("***********************************************************")



    def view_list(self, list_to_view):
        print("--------------------------------------------------------")
        for item in list_to_view:
            print(item)
            print("--------------------------------------------------------")


