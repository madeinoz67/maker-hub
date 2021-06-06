import factory
from faker import Faker
from faker_optional import OptionalProvider
from nanoid import generate

from app.core.config import settings
from app.models.part import PartModel
from app.schema.part import PartPublicSchema  # noqa:
from app.schema.part import PartUpdateSchema  # noqa:
from app.schema.part import PartCreateSchema

Faker.seed(1234)  # reproducible random

fake = Faker()
fake.add_provider(OptionalProvider)

_alphabet = settings.NANOID_ALPHABET
_size = settings.NANOID_SIZE


class PartModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = PartModel

    id = generate(_alphabet, _size)
    name = fake.word()
    description = fake.text()
    footprint = fake.bothify(text="SO?-#", letters="PT")
    manufacturer = fake.company()
    mpn = fake.bothify(text="???-####-###-???")
    notes = fake.text()


class PartCreateSchemaFactory(factory.Factory):
    class Meta:
        model = PartCreateSchema

    name = fake.word()
    description = fake.text()
    footprint = fake.bothify(text="SO?-#", letters="PT")
    manufacturer = fake.company()
    mpn = fake.bothify(text="???-####-###-???")
    notes = fake.text()
