from HelperFunctions import HelperFunctions
from Customer import Customer

class Customers():

    def __init__(self):
        self.customers = []

    def create_customer(self):
        self.customers.append(Customer([customer.id for customer in self.customers]))
        print("Customer created")
        print(self.customers[len(self.customers)-1])

    def view_all_customers(self):
        self.view_customer_list(self.customers)

    def get_current_id(self):
        self.current_id = HelperFunctions.get_valid_id([c.id for c in self.customers], "Enter your customer id:  ")

    def view_self(self):
        print(self.get_customer_by_id(self.current_id))

    def view_customer_list(self, clist):
        if len(clist)>0:
            for c in clist:
                print(c)
        else:
            print("There are no customers to view.")

    def delete_customer(self):
        id = HelperFunctions.get_valid_id([c.id for c in self.customers], "Enter the customer id of the customer you wish to delete:  ")
        if id==0:
            print("No valid customer to delete")
        else:
            print("Customer deleted")
            self.customers = self.delete_customer_by_id(id)

    def delete_customer_by_id(self, id):
        return [c for c in self.customers if c.id != id]

    def get_customer_by_id(self, id):
        return [c for c in self.customers if c.id == id][0]

