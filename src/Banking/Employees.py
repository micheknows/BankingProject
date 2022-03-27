from HelperFunctions import HelperFunctions
from Services import Services
from Customers import Customers
from Accounts import Accounts
from Data import Data


class Employees:

    def view_all_customers(self):
        customers = Customers()
        customers.view_customer_list(customers.customers)

    def create_account(self):
        accounts = Accounts()
        accounts.create_account()

    def add_account_fee(self):
        accounts = Accounts()
        accounts.add_fee()

    def approve_services(self):
        services = Services()
        waiting_list = [service for service in services.services if not service.approved and not service.denied]
        print("\n\nThere are " + str(len(waiting_list)) + " services waiting for a credit decision.\n\n")
        for item in waiting_list:
            print(str(item))
            approve = HelperFunctions.get_string_from_list(["a", "d", "w"], "Please enter a to approve or d to deny this application. (or enter w to wait)")
            if approve == "a":
                item.approve = True
                Data.save_data(services.services, "services")
            elif approve == "d":
                reason = HelperFunctions.get_string("What is the denial reason?")
                item.deny(reason)
                Data.save_data(services.services, "services")


