from models.person import Person

class User(Person):
    def __init__(self, name, email):
        # Call the parent class constructor to pass up common properties
        super().__init__(name)
        self.email = email

    def to_dict(self):
        """Serializes the object data state into a flat JSON dictionary."""
        return {"name": self.name, "email": self.email}

    @classmethod
    def from_dict(cls, data):
        """Reconstructs an active object instance out of dictionary records."""
        return cls(name=data["name"], email=data["email"])

    def __str__(self):
        return f"User: {self.name} (<{self.email}>)"
      
