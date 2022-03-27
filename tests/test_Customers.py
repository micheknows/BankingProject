import sys

sys.path.append("../src/Banking")

from Customers import Customers

def test_create_customer():
    assert Customers.create_customer(Customers()) == None

def test_get_name_by_id():
    # invalid customer ID
    assert Customers.get_name_by_id(Customers(), 150) == ""

def test_view_self():
    # invalid customer ID
    assert Customers.view_self(Customers()) == None

def test_view_customer_list():
    # no customer list
    assert Customers.view_customer_list(Customers(), clist=()) == None

def test_brief_list():
    #no customer list
    assert Customers.brief_list(Customers(), []) == ""

def test_delete_customer_by_id():
    # invalid customer id
    assert len(Customers.delete_customer_by_id(Customers(), 150)) == 3

def test_get_customer_by_id():
    # invalid customer id
    assert Customers.get_customer_by_id(Customers(), 150) == None

def test_save():
    assert Customers.save(Customers()) == None