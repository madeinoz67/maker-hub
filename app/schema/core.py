from pydantic import BaseModel


class CoreSchema(BaseModel):
    """App Base Schema
    Any common logic to be shared with all schema goes here.
    """

    pass


class IDSchemaMixin(BaseModel):
    id: str
