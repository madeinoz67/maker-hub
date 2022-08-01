import datetime
from typing import List

from beanie import Document


class Project(Document):
    id: str
    created_date: datetime.datetime
    last_updated: datetime.datetime
    name: str
    description: str

    # TODO: Project Parts Join
    # if parts is None:
    #     parts = []
    # self.parts = parts


def __repr__(self):
    return f"<Project {self.id}>"
