import sys

sys.path.append("../src/Banking")

from Banking import Banking


def test_create_main_menu():
    assert Banking.create_main_menu() == None

def test_employee_application():
    assert Banking.employee_application() == None

def test_customer_application():
    assert Banking.customer_application() == None

def test_add_item():
    assert Banking.add_item(Banking(), Menu("My Menu"), "New menu item", self.test_customer_application) == None

def test_add_quit():
    assert Banking.add_quit() == None

def test_add_return():
    assert Banking.add_return() == None

def test_return_function():
    assert Banking.return_function() == None

def test_quit_function():
    assert Banking.quit_function() == None

def test_display_menu():
    assert Banking.display_menu() == None
