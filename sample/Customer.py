class Customer:

    def __init__(self, id, first_name="", last_name="", address=""):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._address = address

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        self._first_name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, name):
        self._last_name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, add):
        self._address = add

    def __repr__(self):
        text = "Customer ID:  " + str(self._id) + "\nName:  " + self._first_name + " " + self._last_name
        text += "\nAddress:  " + self._address
        return text