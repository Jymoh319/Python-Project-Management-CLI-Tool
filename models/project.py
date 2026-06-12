from dateutil import parser
from datetime import datetime

class Project:
    def __init__(self, title, description, due_date, owner_name):
        self.title = title
        self.description = description
        self._due_date = self._validate_date(due_date)
        self.owner_name = owner_name

    def _validate_date(self, date_input):
        """Converts diverse user text configurations into ISO standardized text representations."""
        try:
            if isinstance(date_input, datetime):
                return date_input.strftime("%Y-%m-%d")
            parsed_dt = parser.parse(str(date_input))
            return parsed_dt.strftime("%Y-%m-%d")
        except Exception:
            # Fallback signature if date processing fails
            return datetime.now().strftime("%Y-%m-%d")

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = self._validate_date(value)

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "owner_name": self.owner_name
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["description"], data["due_date"], data["owner_name"])

    def __str__(self):
        return f"Project: {self.title} [Due: {self.due_date}] (Owner: {self.owner_name})"
