from beanie import Document


class Location(Document):
    id: str
    name: str


def __repr__(self):
    return f"<Location {self.id}>"
