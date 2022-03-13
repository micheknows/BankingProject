from Customer import Customer
import csv

class Customers():

    def __init__(self, banking):
        self.banking = banking
        self.currentID = -1

        # create the list of customers
        # read existing customers
        self.customers = self.read_customers()
        print(str(len(self.customers)) + " customers loaded..........")



    def get_application_menu(self):
        menu_choices  = {
            "View my profile" : self.view_one_customer,
            "Return to Main Menu" : self.return_main,
            "Quit": self.quit
        }
        menu_name = "Customer Application"

        id = self.currentID
        while id<0:
            print("Enter your customer ID:  ")
            id = int(input())
            if self.get_by_id(id)<0:
                print("That is not a valid customer id, please try again.")
                id = -1
        self.currentID = id
        return [menu_choices, menu_name]


    def get_manage_menu(self):
        # create the menu with function to call on return
        menu_choices = {
            "View Customer List" : self.view_customer_list,
            "Add a new customer" : self.add_customer,
            "View Customer Profile" : self.view_one_customer,
            "Change customer first name" : lambda: self.edit_customer("first name"),
            "Change customer last name" : lambda: self.edit_customer("last name"),
            "Change customer address" : lambda: self.edit_customer("address"),
            "Delete a customer" : self.delete_customer,
            "Return to Previous Menu" : self.return_main,
            "Quit": self.quit
        }
        menu_name = "Customer Management"
        return [menu_choices, menu_name]

    def edit_customer(self, field):
        id =  int(self.ask_property("ID"))
        self.display_one(self.customers[self.get_by_id(id)])
        value = self.ask_property(field)
        if field == "first name":
            self.customers[self.get_by_id(id)].first_name = value
        elif field == "last name":
            self.customers[self.get_by_id(id)].last_name = value
        else:
            self.customers[self.get_by_id(id)].address = value
        self.display_one(self.customers[self.get_by_id(id)])
        self.save()

    def view_customer_list(self):
        print("--------------------------------------------------------")
        for item in self.customers:
            print(item)
            print("--------------------------------------------------------")


    def add_person(self):
        first_name = self.ask_property("first name")
        last_name = self.ask_property("last name")
        return first_name, last_name


    def delete_customer(self):
        id =  int(self.ask_property("ID"))
        self.display_one(self.customers[self.get_by_id(id)])
        if self.sure()==True:
            self.customers.pop(self.get_by_id(id))
            print("Customer Deleted")
        else:
            print("Customer NOT Deleted")
        self.save()

    def sure(self):
        print("Are you sure? (Enter Y for yes)")
        if input()=="Y":
            return True
        else:
            return False


    def add_customer(self):
        first = None
        while first is None or self.exists(first,last):
            first, last = self.add_person()
        print("What is the address?")
        address = input()
        c = Customer(self.get_next_id(), first, last, address)
        print(repr(c))
        self.customers.append(c)
        self.save()


    def delete_customer(self):
        pass

    def return_main(self):
        self.banking.location = "return"
        self.banking.previous_menu()

    def quit(self):
        self.banking.location="quit"

    def view_one_customer(self):
        if (self.currentID<0):
            id = int(self.ask_property("ID"))
        else:
            id = self.currentID
        self.display_one(self.customers[self.get_by_id(id)])
        self.banking.location = "testing"


    def display_one(self, item):
        print("***********************************************************")
        print(item)
        print("***********************************************************")


    def ask_property(self, prop):
        print("Enter the " + prop + ":  ")
        return input()


    def get_by_id(self, id):
        for index, item in enumerate(self.customers):
            if item.id==id:
                return index
        return -1

    def read_customers(self):
        customers = []
        with open("customers.csv", "r") as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                if len(line)>0:
                    customers.append(Customer(int(line[0]), line[1], line[2], line[3]))
        return customers


    def save(self):
        try:
            with open("customers.csv", "w") as f:
                writer = csv.writer(f)
                for item in self.customers:
                    writer.writerow([item.id, item.first_name, item.last_name, item.address])
        except BaseException as e:
            print("BaseException while saving:  ", "customers.csv")


    def get_next_id(self):
        id = 0
        for item in self.customers:
            if item.id > id:
                id = item.id
        return (id + 1)


    def exists(self, first, last):
        for customer in self.customers:
            if customer.first_name==first and customer.last_name==last:
                print("That customer already exists.  Please try again.")
                return True
        return False


