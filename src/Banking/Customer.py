


class Customer:

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, fname):
        self._firstname = fname

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lname):
        self._lastname = lname

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, add):
        self._address = add

