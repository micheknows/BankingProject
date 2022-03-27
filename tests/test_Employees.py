import sys

sys.path.append("../src/Banking")

from Employees import Employees


def test_view_all_customers():
    assert Employees.view_all_customers(Employees()) == None

def test_create_account():
    assert Employees.create_account(Employees()) == None

def test_add_account_fee():
    assert Employees.add_account_fee(Employees()) == None

def test_approve_services():
    assert Employees.approve_services(Employees()) == None