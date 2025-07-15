
import re

def name_validator(name):
        if not (type(name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", name)):
            raise ValueError("Invalid name")

def family_validator(family):
        if not (type(family) == str and re.match(r"^[a-zA-Z\s]{3,30}$", family)):
            raise ValueError("Invalid family")

def age_validator(age):
        if not (type(age) == int and 0 < age < 150):
            raise ValueError("Invalid age")

