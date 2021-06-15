#
# Copyright 2021 Stephen Eaton
#
# This file is part of Maker-Hub.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights,
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from sqlalchemy.ext.asyncio import AsyncSession


class CoreService:
    """CoreService Class.

    Any common logic to be shared with all Services goes here
    """

    def __init__(self) -> None:
        """Initialize the base Service Class ."""
        pass


class BaseDBService(CoreService):
    """DataBase Service Base Class.

    Any common logic to be shared with all Services goes here

    """

    def __init__(self, db: AsyncSession) -> None:
        """Initialize the Database service.

        Args:
            db (Database): Database Session
        """
        super().__init__()
        self.db = db


class BaseRemoteService(CoreService):
    """Remote Service Base Class.

    Any common logic to be shared with all Services goes here

    """

    def __init__(self) -> None:
        """Remote Service initialise ."""
        super().__init__()
