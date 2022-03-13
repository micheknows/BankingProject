from Account import Account
import csv

class Accounts:

    def __init__(self, banking):
        self.banking = banking
        self.accounts= self.read_accounts()
        print(str(len(self.accounts)) + " accounts loaded..........")

    def get_manage_menu(self):
        # create the menu with function to call on return
        menu_choices = {
            "Create Account" : self.create_account,
            "Delete Account" : self.delete_account,
            "Display Customer Accounts" : self.display_accounts,
            "Return to Previous Menu" : self.return_previous,
            "Return to Main Menu" : self.return_main,
            "Quit": self.quit
        }
        menu_name = "Account Management"
        return [menu_choices, menu_name]

    def deposit(self, customer_id):
        self.display_accounts_by_customer_id(customer_id)
        id = int(self.ask_question("account ID"))
        while not self.id_exists(id) or self.accounts[self.get_by_id(id)].customer_id!=customer_id:
            print("That account does not exist for customer's profile, please try again (or enter Q to quit)")
            id = int(self.ask_question("account ID"))
            if (id=="Q"):
                self.banking.location = "return"
                self.banking.previous_menu()
                break
        amount = float(self.ask_question(" amount to deposit"))
        self.accounts[self.get_by_id(id)].balance = self.accounts[self.get_by_id(id)].balance + amount
        print("Deposit Entered")
        self.display_accounts_by_customer_id(customer_id)


    def id_exists(self, id):
        for account in self.accounts:
            if account.id==id:
                return True
        return False

    def withdraw(self, customer_id):
        self.display_accounts_by_customer_id(customer_id)
        id = int(self.ask_question("account ID"))
        while not self.id_exists(id) or self.accounts[self.get_by_id(id)].customer_id!=customer_id:
            print("That account does not exist for customer's profile, please try again (or enter Q to quit)")
            id = int(self.ask_question("account ID"))
            if (id=="Q"):
                self.banking.location = "return"
                self.banking.previous_menu()
                break
        amount = float(self.ask_question(" amount to withdraw"))
        self.accounts[self.get_by_id(id)].balance = self.accounts[self.get_by_id(id)].balance - amount
        print("Withdrawal Processed")
        self.display_accounts_by_customer_id(customer_id)



    def sure(self):
        print("Are you sure? (Enter Y for yes)")
        if input()=="Y":
            return True
        else:
            return False


    def get_by_id(self, id):
        for index, item in enumerate(self.accounts):
            if item.id==id:
                return index
        return -1


    def delete_account(self):
        id = int(self.ask_question((" account id")))
        print(self.accounts[self.get_by_id(id)])
        if self.sure()==True:
            self.accounts.pop(self.get_by_id(id))
            print("Account Deleted")
        else:
            print("Account NOT Deleted")
        self.save()

    def display_accounts(self):
        id = int(self.ask_question("customer ID"))
        while not self.banking.customers.id_exists(id):
            print("That customer does not exist, please try again (or enter Q to quit)")
            id = int(self.ask_question("customer ID"))
            if (id=="Q"):
                self.banking.location = "return"
                self.banking.previous_menu()
                break
        self.display_accounts_by_customer_id(id)

    def display_accounts_by_customer_id(self, id):
        count = 0
        print("*****************************************")
        print(self.banking.get_customer(id))
        print("*****************************************")
        for account in self.accounts:
            if account._customer_id == id:
                count += 1
                print(account)
                print("*****************************************")
        print("Number of accounts:  " + str(count))
        print("*****************************************")
        print("*****************************************")
        print("")
        print("")
        print("")


    def create_account(self):
        id = int(self.ask_question("customer ID"))
        while not self.banking.customers.id_exists(id):
            print("That customer does not exist, please try again (or enter Q to quit)")
            id = int(self.ask_question("customer ID"))
            if (id=="Q"):
                self.banking.location = "return"
                self.banking.previous_menu()
                break
        account_type = self.ask_question("type of account (savings or checking)").lower()
        while account_type!="checking" and account_type!="savings":
            print("Please enter checking or savings (or enter Q to quit)")
            account_type = self.ask_question("type of account (savings or checking)").lower()
            if (account_type=="Q"):
                self.banking.location = "return"
                self.banking.previous_menu()
                break
        dep = self.ask_question("customer's initial deposit")
        try:
            deposit = float(dep)
        except:
            deposit = 0
        self.accounts.append(Account(self.banking, self.get_next_id(), id, account_type, deposit))
        print(repr(self.accounts[len(self.accounts)-1]))
        self.save()



    def get_next_id(self):
        id = 0
        for item in self.accounts:
            if item.id > id:
                id = item.id
        return (id + 1)



    def ask_question(self, prop):
        print("Enter the " + prop + ":  ")
        return input()



    def return_main(self):
        self.banking.location = "return"
        self.banking.main_menu()

    def return_previous(self):
        self.banking.location = "return"
        self.banking.previous_menu()

    def quit(self):
        self.banking.location="quit"


    def read_accounts(self):
        accounts = []
        try:
            with open("accounts.csv", "r") as f:
                csv_reader = csv.reader(f)
                for line in csv_reader:
                    if len(line)>0:
                        accounts.append(Account(self.banking, int(line[0]), int(line[1]), line[2], float(line[3])))
        except BaseException as e:
            print("exception " + repr(e))
            accounts = []
        return accounts


    def save(self):
        try:
            with open("accounts.csv", "w") as f:
                writer = csv.writer(f)
                for item in self.accounts:
                    writer.writerow([item.id, item.customer_id, item.account_type, item.balance])
        except BaseException as e:
            print("BaseException while saving:  ", "customers.csv")
            print(repr(e))

