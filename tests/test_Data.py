import sys

sys.path.append("../src/Banking")

from Data import Data


def test_get_valid_account_by_customer_id():
    # invalid customer id is supplied
    assert Accounts.get_valid_account_by_customer_id(152) == 0

def test_save_data():
    #empty data
    assert Data.save_data([], "test") == None

def test_retrieve_datat():
    assert len(Data.retrieve_data("customers")) == 3