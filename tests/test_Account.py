import sys

sys.path.append("../src/Banking")

from Account import Account


def test_account():
    """ invalid customer id assigned at creation"""
    a = Account(3, 105, 'checking', 21.32)
    assert str(a) == "\n\n**********\n\nACCOUNT ID:  3\nERROR:  THIS ACCOUNT IS NOT ASSOCIATED WITH A VALID CUSTOMER \nAccount Type:  checking\nBalance:  $21.32"
