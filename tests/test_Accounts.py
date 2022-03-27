import sys
sys.path.append("../src/Banking")
from Accounts import Accounts


def test_get_valid_account_by_customer_id():
    # invalid customer id is supplied
    assert Accounts.get_valid_account_by_customer_id(152) == 0

def test_view_customer_accounts():
    #invalid customer id is supplied
    assert Accounts.view_customer_accounts(Accounts(),105) == None

def test_get_valid_customer():
    # no data exists
    assert Accounts.get_valid_customer() == 0

def test_create_account():
    # no customer id supplied
    assert Accounts.create_account(customer_id="") == None
    # invalid customer id is supplied
    assert Accounts.create_account(customer_id=150) == None

def test_get_account_by_id():
    # invalid account id
    assert Accounts.get_account_by_id(Accounts(), 150) == 0

def test_transaction():
    #invalid account id supplied
    assert Accounts.transaction(Accounts(), 150, 32.15) == None

def test_get_account_list_by_customer_id():
    #invalid customer id entered
    assert Accounts.get_account_list_by_customer_id(Accounts(), 150) == []

def test_view_account_list():
    # empty account list supplied
    assert Accounts.view_account_list(Accounts(), []) == None

def test_save():
    assert Accounts.save(Accounts()) == None

