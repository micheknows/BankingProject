from Menus import Menus


class UserInteractions:

    def display_menu(self, menus):
        print(menus)
        choice = input()
        return int(choice)

