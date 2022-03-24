class Menus:

    def build_menu(choices, location):
        text = "\n\n" + location + " Menu\n"
        text += "Please enter your choice by the number:\n\n"
        for index, choice in enumerate(choices,1):
            text = text + str(index) + ".  " + choice + "\n"
        return text
