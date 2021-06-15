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

"""factory.py.

Factory module to create the required model and schema factories for testing
"""

import datetime
import random

import factory
from faker import Faker
from faker_optional import OptionalProvider  # noqa:
from nanoid import generate

from app.core.config import settings
from app.models.part import PartModel
from app.schema.part import PartPublicSchema  # noqa:
from app.schema.part import PartUpdateSchema  # noqa:
from app.schema.part import PartCreateSchema
from tests import common

_alphabet = settings.NANOID_ALPHABET
_size = settings.NANOID_SIZE

fake = Faker()


def nanoid() -> str:
    """Nanoid generation wrapper.

    Returns:
        str: nanoid
    """
    return generate(_alphabet, _size)


class PartModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Factory for creating PartModel DB objects .

    Returns:
        [PartModel]: A PartModel instance
    """

    class Meta:
        """Class decorator for creating the PartModelFactory."""

        model = PartModel
        sqlalchemy_session = common.async_session

    id: str = factory.LazyFunction(nanoid)
    name: str = factory.Sequence(lambda n: f"part-{n}")
    description: str = factory.Faker("text", max_nb_chars=random.randint(20, 150))
    footprint: str = factory.Faker("bothify", text="SO?-#", letters="PT")
    manufacturer: str = fake.company()
    mpn: str = factory.Faker("bothify", text="???-####-###-???")
    notes: str = factory.Faker("text", max_nb_chars=random.randint(50, 300))
    created_at = factory.Faker("past_datetime", start_date="-60d")
    updated_at = datetime.datetime.now()


class PartCreateSchemaFactory(factory.Factory):
    """Factory for creating PartCreateSchema object instances for testing.

    Returns:
        [PartCreateSchema]: A PartCreateSchema object instance
    """

    class Meta:
        """Class decorator for creating the PartCreateSchemaFactory."""

        model = PartCreateSchema

    name: str = factory.Sequence(lambda n: f"part-{n}")
    description: str = factory.Faker("text", max_nb_chars=random.randint(20, 150))
    footprint: str = factory.Faker("bothify", text="SO?-#", letters="PT")
    manufacturer: str = factory.Faker("company")
    mpn: str = factory.Faker("bothify", text="???-####-###-???")
    notes: str = factory.Faker("text", max_nb_chars=random.randint(50, 300))

    def __str__(self):
        """To string.

        Returns:
            [str]:
        """
        return f"{self.name}"
