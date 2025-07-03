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

    def username (self):
        return f"{self.username}"

    def __repr__(self):
        return f"{self.username()} {self.full_name()}"

    def to_tuple(self):
        return tuple(self.username().values())


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        name_validator(value)
        self._name = value
