from fastapi import HTTPException, status


class DuplicatedEntryError(HTTPException):
    def __init__(self, message: str = "A key already exists"):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=message
        )


class NoResultsFound(HTTPException):
    def __init__(self, message: str = "No Results Found"):
        super().__init__(status_code=status.HTTP_200_OK, detail=message)
