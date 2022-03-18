from HelperFunctions import ManageVariables

class ServiceFunctions:

    def __init__(self):
        self.services = []
        self.read()
        self.mv = ManageVariables()

    def createLoan(self,customer_id, limit, balance, number_months):
        self.mv.get_next_id(self.mv.get_id_list(self.services))

    def save(self):
        templist = [[item.id, item.customer_id, item.account_type, item.balance] for item in self.accounts]
        mv = ManageVariables()
        mv.save_variables(templist,"accounts")

    def read(self):
        templist = self.mv.read("services")
        accounts = [[int(item[0]), int(item[1]), item[2], float(item[3])] for item in templist if len(item)>0]
        for account in accounts:
            self.accounts.append(Accounts(account[1], account[3], account[2], account[0]))
