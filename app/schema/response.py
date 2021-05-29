from typing import Optional

from pydantic import BaseModel, HttpUrl


class BaseResponseBody(BaseModel):
    status: int = 200
    code: Optional[int] = None
    property: Optional[str] = None
    message: Optional[str] = None
    developerMessage: Optional[str] = None
    moreInfo: Optional[HttpUrl] = None
