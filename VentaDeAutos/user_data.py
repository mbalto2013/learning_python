class cls_user_info:
    def __init__(self, ssn, name, last_name_1, last_name_2, dob):
        self._ssn = ssn
        self._name = name
        self._last_name_1 = last_name_1
        self._last_name_2 = last_name_2
        self._dob = dob

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    @property
    def ssn(self):
        return self._ssn

    @ssn.setter
    def ssn(self, new_ssn):
        self._ssn = new_ssn

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def last_name_1(self):
        return self._last_name_1

    @last_name_1.setter
    def name(self, new_last_name_1):
        self._last_name_1 = new_last_name_1

    @property
    def last_name_2(self):
        return self._last_name_2

    @last_name_2.setter
    def name(self, new_last_name_2):
        self._last_name_2 = new_last_name_2

    @property
    def dob(self):
        return self._dob

    @ssn.setter
    def ssn(self, dob):
        self._dob = new_dob