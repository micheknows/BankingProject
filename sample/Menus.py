class Menus:

    def __init__(self,menu_choices, menu_name):
        # receive a list of menu choices and the menu name
        self.menu_choices = menu_choices
        self.name = menu_name

    def display_menu(self):
        menu_choice = ""
        while self.mk_int(menu_choice)-1 not in range(len(self.menu_choices)):
            print(self.name + " Menu")
            print("Enter the number for your choice of action:")
            for index, choice in enumerate(self.menu_choices,1):
                print(str(index) + ".  " + choice)
            menu_choice = input()
        return self.menu_choices[int(menu_choice)-1]


    def mk_int(self,s):
        try:
            return int(s)
        except:
            return 0