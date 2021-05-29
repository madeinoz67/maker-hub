from databases import Database


class CoreService:
    """CoreService

    Any common logic to be shared with all Services goes here

    """

    def __init__(self) -> None:
        pass


class BaseDBService(CoreService):
    """DataBase Service Base Class

    Any common logic to be shared with all Services goes here

    """

    def __init__(self, db: Database) -> None:
        super().__init__()
        self.db


class BaseRemoteService(CoreService):
    """Remote Service Base Class

    Any common logic to be shared with all Services goes here

    """

    def __init__(self) -> None:
        super().__init__()
