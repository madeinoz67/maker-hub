from pydantic import BaseModel


class Part(BaseModel):
    id: str
    name: str
    description: str
