import sys

sys.path.append("../src/Banking")

from Accounts import Accounts


def test_accounts():
    """ nothing assigned at creation"""
    a = Accounts()
    assert str(a) == "Account ID:  " + str(1) + "\nCustomer ID:  " + str(1) + "\nBalance:  " + "${:,.2f}".format(
        0) + "\n***************************************************\n"

    """ ID assigned """
    a = Accounts(id=43)
    assert str(a) == "Account ID:  " + str(43) + "\nCustomer ID:  " + str(1) + "\nBalance:  " + "${:,.2f}".format(
        0) + "\n***************************************************\n"


def test_assign_id():
    a = Accounts()
    assert a.assign_id() == 1

