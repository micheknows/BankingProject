from Persons import Persons
from Customer import Customer
import csv

class Customers(Persons):

    def __init__(self):
        self.quit_now = False
        self.return_now = False

        # create the list of customers
        # read existing customers
        self.customers = self.read_customers()
        print(str(len(self.customers)) + " customers loaded..........")


        # create the menu with function to call on return
        self.menu_choices = {
            "View Customer List" : self.view_customer_list,
            "Add a new customer" : self.add_customer,
            "View a customer" : self.view_one_customer,
            "Change customer first name" : self.change_customer_fname,
            "Change customer last name" : self.change_customer_lname,
            "Change customer address" : self.change_customer_address,
            "Delete a customer" : self.delete_customer,
            "Return to Main Menu" : self.return_main,
            "Quit": self.quit
        }
        super().__init__(self.menu_choices,"Customer")

    def view_one_customer(self):
        super().display_one(self.customers[super().get_by_id(self.customers, super().ask_id())])

    def delete_customer(self):
        id = super().ask_id()
        super().display_one(self.customers[super().get_by_id(self.customers, id)])
        if super().sure()==True:
            self.customers.pop(super().get_by_id(self.customers, id))
            print("Customer Deleted")
        else:
            print("Customer NOT Deleted")
        self.save()

    def change_customer_fname(self):
        id = super().ask_id()
        super().display_one(self.customers[super().get_by_id(self.customers, id)])
        self.customers[super().get_by_id(self.customers, id)].first_name = super().ask_property("First Name")
        super().display_one(self.customers[super().get_by_id(self.customers, id)])
        self.save()

    def change_customer_lname(self):
        id = super().ask_id()
        super().display_one(self.customers[super().get_by_id(self.customers, id)])
        self.customers[super().get_by_id(self.customers, id)].last_name = super().ask_property("Last Name")
        super().display_one(self.customers[super().get_by_id(self.customers, id)])
        self.save()

    def change_customer_address(self):
        id = super().ask_id()
        super().display_one(self.customers[super().get_by_id(self.customers, id)])
        self.customers[super().get_by_id(self.customers, id)].address = super().ask_property("Address")
        super().display_one(self.customers[super().get_by_id(self.customers, id)])
        self.save()

    def view_customer_list(self):
        super().view_list(self.customers)

    def add_customer(self):
        first = None
        while first is None or self.exists(first,last):
            first, last = super().add_person()
        print("What is the address?")
        address = input()
        c = Customer(super().get_next_id(self.customers), first, last, address)
        print(repr(c))
        self.customers.append(c)
        self.save()


    def exists(self, first, last):
        for customer in self.customers:
            if customer.first_name==first and customer.last_name==last:
                print("That customer already exists.  Please try again.")
                return True
        return False

    def dummy_function(self):
        print("I'm a dummy")

    def quit(self):
        self.quit_now = True

    def return_main(self):
        self.return_now = True

    def save(self):
        try:
            with open("customers.csv", "w") as f:
                writer = csv.writer(f)
                for item in self.customers:
                    writer.writerow([item.id, item.first_name, item.last_name, item.address])
        except BaseException as e:
            print("BaseException while saving:  ", "customers.csv")

    def read_customers(self):
        customers = []
        with open("customers.csv", "r") as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                if len(line)>0:
                    customers.append(Customer(int(line[0]), line[1], line[2], line[3]))
        return customers


