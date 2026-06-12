"""Defines core human characteristics to handle inheritance validation checks."""

class Person:
    def __init__(self, name):
        self._name = name  # Encapsulated protected attribute

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Name attribute must be a valid, non-empty string structure.")
        self._name = value.strip()
