from HelperFunctions import HelperFunctions
from Customer import Customer
from Data import Data

class Customers():

    def __init__(self):
        self.customers = Data.retrieve_data("customers")

    def create_customer(self):
        self.customers.append(Customer([customer.id for customer in self.customers]))
        print("Customer created")
        print(self.customers[len(self.customers)-1])
        self.save()

    def view_self_accounts(self, accounts):
        accounts.view_account_list(accounts.get_account_list_by_customer_id(self.current_id))

    def make_account_transaction(self, accounts):
        transaction_types = ["deposit", "withdraw"]
        print("Here are your active accounts:")
        accounts.view_account_list(accounts.get_account_list_by_customer_id(self.current_id))
        account_id = HelperFunctions.get_valid_id([a.id for a in accounts.accounts if a.customer_id==self.current_id], "Enter the account id:  ")
        if account_id > 0:
            transaction_type = HelperFunctions.get_string_from_list([s[0] for s in transaction_types],"Enter the first letter of the transaction type " + repr(transaction_types) + ":  ")
            if transaction_type != "@":
                amt = HelperFunctions.get_float("For how much?")
                if transaction_type == "w":
                    amt = amt * -1
                previous_balance = accounts.get_account_by_id(account_id).balance
                accounts.transaction(account_id, amt)
                print([t for t in transaction_types if t.startswith(transaction_type.lower())][0].capitalize() + " successful in the amount of $" + HelperFunctions.format_currency(amt) )
                print("Previous balance:  $" + HelperFunctions.format_currency(previous_balance))
                print("New balance:  $" + HelperFunctions.format_currency(accounts.get_account_by_id(account_id).balance))



    def view_all_customers(self):
        self.view_customer_list(self.customers)

    def get_name_by_id(self, id):
        return [c.first_name + " " + c.last_name for c in self.customers if c.id==id][0]

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
            save()

    def delete_customer_by_id(self, id):
        return [c for c in self.customers if c.id != id]

    def get_customer_by_id(self, id):
        return [c for c in self.customers if c.id == id][0]

    def save(self):
        Data.save_data(self.customers, "customers")
