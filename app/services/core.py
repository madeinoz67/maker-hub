class CoreService:
    """CoreService

    Any common logic to be shared with all Services goes here

    """

    def __init__(self):
        pass


class BaseDBService(CoreService):
    """DataBase Service Base Class

    Any common logic to be shared with all Services goes here

    """

    def __init__(self):
        super().__init__()


class BaseRemoteService(CoreService):
    """Remote Service Base Class

    Any common logic to be shared with all Services goes here

    """

    def __init__(self):
        super().__init__()
