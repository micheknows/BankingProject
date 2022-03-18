from HelperFunctions import ManageVariables
from Services import Loans
from Services import credit_cards

class ServiceFunctions:

    def __init__(self):
        self.services = []
        self.mv = ManageVariables()
        self.read()

    def createLoan(self,customer_id, limit, balance, number_months):
        loan = Loans(self.mv.get_next_id(self.mv.get_id_list(self.services)), customer_id, limit, balance, number_months)
        self.services.append(loan)
        print(str(loan))
        self.save()

    def get_customer_loans(self, customer_id):
        return [service for service in self.services if type(service)==Loans and service.customer_id==customer_id]

    def create_credit_card(self,customer_id, limit, balance):
        cc = credit_cards(self.mv.get_next_id(self.mv.get_id_list(self.services)), customer_id, limit, balance)
        self.services.append(cc)
        print(str(cc))
        self.save()

    def get_customer_ccs(self, customer_id):
        return [service for service in self.services if type(service)==credit_cards and service.customer_id==customer_id]

    def save(self):
        loanlist = [[item.id, item.customer_id, item.limit, item.balance, item.number_months] for item in self.services if type(item)==Loans]
        self.mv.save_variables(loanlist,"loans")
        ccslist = [[item.id, item.customer_id, item.limit, item.balance] for item in self.services if type(item)==credit_cards]
        self.mv.save_variables(ccslist,"ccs")

    def read(self):
        loanlist = self.mv.read("loans")
        loans = [[int(item[0]), int(item[1]), float(item[2]), float(item[3]), int(item[4])] for item in loanlist if len(item)>0]
        for loan in loans:
            id = loan[0]
            cid = loan[1]
            limit = loan[2]
            bal = loan[3]
            num = loan[4]
            self.services.append(Loans(id, cid, limit, bal, num))
        cclist = self.mv.read("ccs")
        ccs = [[int(item[0]), int(item[1]), float(item[2]), float(item[3])] for item in cclist if len(item)>0]
        for cc in ccs:
            self.services.append(credit_cards(cc[0], cc[1], cc[2], cc[3]))

