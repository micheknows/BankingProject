import sys

sys.path.append("../src/Banking")

from Services import Services


def test_apply_service():
    # invalid customer ID
    assert Services.apply_service(Services(), 'loan', 150) == None

def test_view_services_list():
    # invalid customer ID
    assert Services.view_services_list(Services(), 150) == None
