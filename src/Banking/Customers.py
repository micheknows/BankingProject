from HelperFunctions import ManageVariables

class Customers:

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        self._firstname = firstname

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname


    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    def __init__(self, firstname="", lastname="", address="", id=""):
        self.customers = []
        self.mv = ManageVariables()
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.address = address

    def __str__(self):
        text = "Customer ID:  " + str(self.id)
        text += "\nCustomer Name:  " + self.firstname + " " + self.lastname
        text += "\nAddress:  " + self.address
        text += "\n***************************************************\n"
        return text;

