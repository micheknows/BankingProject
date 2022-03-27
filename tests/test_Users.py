import sys

sys.path.append("../src/Banking")

from Users import Users


def test_create_main_menu():
    assert Users.create_main_menu() == None

def test_employee_application():
    assert Users.employee_application() == None

def test_customer_application():
    assert Users.customer_application() == None

def test_add_item():
    assert Users.add_item(Users(), Menu("My Menu"), "New menu item", self.test_customer_application) == None

def test_add_quit():
    assert Users.add_quit() == None

def test_add_return():
    assert Users.add_return() == None

def test_return_function():
    assert Users.return_function() == None

def test_quit_function():
    assert Users.quit_function() == None

def test_display_menu():
    assert Users.display_menu() == None
