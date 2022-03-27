from HelperFunctions import HelperFunctions
from Customer import Customer
from Data import Data
from Services import Services


class Customers:

    def __init__(self):
        self.customers = Data.retrieve_data("customers")

    def create_customer(self):
        self.customers.append(Customer([customer.id for customer in self.customers]))
        print("Customer created")
        print(self.customers[len(self.customers)-1])
        self.save()

    def view_self_services(self):
        services = Services()
        services.view_services_list(self.current_id)

    def apply_service(self, service_type):
        services = Services()
        amt = HelperFunctions.get_float("How much do you want to apply for?")
        if amt > 0:
            if service_type == "loan":
                purpose = HelperFunctions.get_string("What is the purpose of the loan?")
            else:
                purpose=""
            services.apply_service(service_type, amt, self.current_id, self, purpose)

    def get_name_by_id(self, id):
        return [c.first_name + " " + c.last_name for c in self.customers if c.id == id][0]

    def get_current_id(self):
        self.current_id = HelperFunctions.get_valid_id([c.id for c in self.customers], "Enter your customer id:  ")

    def view_self(self):
        print(self.get_customer_by_id(self.current_id))

    def view_customer_list(self, clist):
        if len(clist) > 0:
            for c in clist:
                print(c)
        else:
            print("There are no customers to view.")

    def delete_customer(self):
        id = HelperFunctions.get_valid_id([c.id for c in self.customers], "Enter the customer id of the customer you "
                                                                          "wish to delete:  ")
        if id == 0:
            print("No valid customer to delete")
        else:
            print("Customer deleted")
            self.customers = self.delete_customer_by_id(id)
            self.save()

    def delete_customer_by_id(self, id):
        return [c for c in self.customers if c.id != id]

    def get_customer_by_id(self, id):
        return [c for c in self.customers if c.id == id][0]

    def save(self):
        Data.save_data(self.customers, "customers")
