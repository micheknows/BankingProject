class Customer:

    @property
    def fname(self):
        return self._fname

    @fname.setter
    def fname(self, fn):
        self._fname = fn

    @property
    def lname(self):
        return self._lname

    @lname.setter
    def lname(self, ln):
        self._lname = ln

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, add):
        self._address = add

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    def __init__(self, id, fname, lname, address, email):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.address = address
        self.email = email

    def __str__(self):
        text = "\n\nCUSTOMER"
        text = text + "  ID:  " + str(self.id) + "\n"
        text = text + "Name:  " + self.fname + " " + self.lname +  "\n"
        text = text + "Address:  " + self.address + "\n"
        text = text + "Email:  " + self.email + "\n"
        return text

