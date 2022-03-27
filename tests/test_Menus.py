import sys

sys.path.append("../src/Banking")

from Menus import Menus


def test_add_item():
    assert Menus.add_item(Menus("My Menu"), "Menu description") == None

def test_add_return():
    assert Menus.add_return(Menus("My Menu")) == None

def test_add_quit():
    assert Menus.add_quit(Menus("My Menu")) == None