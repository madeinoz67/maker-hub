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
    """Wrapper for nanoid generation

    Returns:
        str: nanoid
    """
    return generate(_alphabet, _size)


class PartModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
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
    class Meta:
        model = PartCreateSchema

    name: str = factory.Sequence(lambda n: f"part-{n}")
    description: str = factory.Faker("text", max_nb_chars=random.randint(20, 150))
    footprint: str = factory.Faker("bothify", text="SO?-#", letters="PT")
    manufacturer: str = factory.Faker("company")
    mpn: str = factory.Faker("bothify", text="???-####-###-???")
    notes: str = factory.Faker("text", max_nb_chars=random.randint(50, 300))

    def __str__(self):
        return f"{self.name}"
