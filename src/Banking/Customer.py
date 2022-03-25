from HelperFunctions import HelperFunctions

class Customer:


    def __init__(self, id_list):
        self.id = HelperFunctions.get_next_id(id_list)
        self.first_name = HelperFunctions.get_string("Please enter the customer's first name:  ")
        self.last_name = HelperFunctions.get_string("Please enter the customer's last name:  ")
        self.address = HelperFunctions.get_string("Please enter the customer's address:  ")


    def __str__(self):
        text = "\n\n**********\n\nCUSTOMER ID:  " + str(self.id)
        text = text + "\nName:  " + self.first_name + " " + self.last_name
        text = text + "\nAddress:  " + self.address
        return text
