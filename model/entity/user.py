from altair import value

from model.tools.validation import name_validator


class User:
    def __init__(self, name,family ,birth_date, username, role, password,is_locked):
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.username = username
        self.role = role


    def full_name(self):
        return f"{self._name} {self._family}"

    def __repr__(self):
        return f"{self.full_name()} {self.birth_date} date"

    def to_tuple(self):
        return (self.name, self.family, self.birth_date, self.username, self.role, )

    def get_name (self):
        return self.name

    def __repr__(self):
        return f"{self.username()} {self.full_name()}"

    def to_tuple(self):
        return tuple(self.username().values())

    def set_name(self, value):
        self._name = value

    def get_family(self):
        return self.family

    def set_family(self, value):
        self._family = value

    def get_user_name(self):
        return self.username
    def set_user_name(self, value):
        self._username = value

    def get_password(self):
        return self._password

    def set_password(self, value):
        self._password = value

    def get_role(self):
        return self.role()

    def set_role(self, value):
        self._role = value

    def is_locked(self):
        self._is_locked = value

    def set_is_locked(self, value):
        self._is_locked = value



    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        name_validator(value)
        self._name = value
