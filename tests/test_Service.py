import sys

sys.path.append("../src/Banking")

from Service import Service
from Service import Loan
from Service import CreditCard
from Customers import Customers


def test_deny_app():
    assert Service.deny_app(Service(1,1,Customers(), 0),  "Just because") == None

def test_approval_message():
    # not approved (hasn't gone through approval process)
    assert Service.approval_message(Service(1,1,Customers(), 0)) == "\n\nYOUR APPLICATION FOR THE FOLLOWING IS PROCESSING.  WE WILL INFORM YOU OF OUR CREDIT DECISION.\n\n "
    # denied
    s = Service(1,1,Customers(), 0)
    s.deny_app("Just because")
    s.denied = True
    assert s.approval_message() == "\n\nWe are sorry to inform you that this application was denied.\n\n"

def test_deny():
    #Loans
    assert Loan.deny(Loan(1, 1, 32.43, Customers(), "buy car"),"credit score") == None
    #CreditCards
    assert CreditCard.deny(CreditCard(1, 1, 32.43, Customers()),"credit score") == None
