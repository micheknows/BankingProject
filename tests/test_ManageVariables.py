import sys
sys.path.append("../src/Banking")

from ManageVariables  import ManageVariables

def test_get_next_id():
    """ pass a list of integers should give next highest integer"""
    mv = ManageVariables()
    assert mv.get_next_id([1,2,3]) == 4
