from Menus import Menus
from UserInteractions import UserInteractions as ui
from Customer import Customer
from Account import Account

class Banking:

    def __init__(self):
        self.do_main_menu()
        self.quit = False
        self.customers = []
        self.accounts = []

    def show_menu(self):
        print(Menus.build_menu(self.menu_choices, self.menu_location))
        choice = int(input())
        list(self.menu_choices.values())[choice-1]()

    def emp_menu(self):
        self.menu_choices = {
                                "View All Customers": lambda : self.view_all_in_list(self.customers, "customers"),
                                "Create a Customer" : self.create_customer,
                                "Delete a Customer" : lambda : self.delete_from_list(self.customers, "customers"),
                                "View All Accounts" : lambda : self.view_all_in_list(self.accounts, "accounts"),
                                "Create an Account" : self.create_account,
                                "Return to Main Menu" : self.do_main_menu,
                                "Quit" : self.quit_now
                            }
        self.menu_location = "Employee"

    def create_customer(self):
        self.customers.append(Customer(self.get_next_id(self.customers), ui.get_string("What is the customer's first name?"), ui.get_string("What is the customer's last name?"), ui.get_string("What is the customer's address?"), ui.get_string("What is the customer's email?")))
        print("Customer added")
        self.view_last_in_list(self.customers, "customers")

    def create_account(self):
        if len(self.customers)>0:
            customer_id = ui.get_valid_from_list(self.customers)
            if customer_id > -1:
                self.accounts.append(Account(self.get_next_id(self.accounts), ui.get_item_by_id(self.customers,customer_id), ui.get_string_in_items("What type of account?  Please enter c for checking or s for savings", ['c','s']),ui.get_float("What is the initial deposit into the account?")))
                print("Account created")
                self.view_last_in_list(self.accounts,"accounts")
            else:
                print("That is not a valid customer to use.")
        else:
            print("There are no customers to create accounts for.")

    def view_last_in_list(self, obj_list, obj_name):
        if (len(obj_list)>0):
            print(str(obj_list[len(obj_list)-1]))
        else:
            print("There are no " + obj_name + " in the data.")


    def view_all_in_list(self, obj_list, obj_name):
        if len(obj_list)>0:
            for obj in obj_list:
                print(str(obj))
        else:
            print("There are no " + obj_name + " in the data.")

    def delete_from_list(self, obj_list, obj_name):
        self.view_all_in_list(obj_list, obj_name)
        index = ui.get_integer("Enter the number of the customer to delete: ")-1
        obj_list.pop(index)
        print("Deleted")
        for item in obj_list:
            print(str(item))

    def get_next_id(self, obj_list):
        current_id = 1
        for obj in obj_list:
            if obj.id >= current_id:
                current_id = obj.id + 1
        return current_id

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