import re


def code_validator(code):
    if not (type(code) == int and code > 0):
        raise ValueError("Invalid Code !!!                                                                                                                                                                                                                                                                    ")

