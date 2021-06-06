import factory
from faker import Faker
from faker_optional import OptionalProvider

from app.schema.part import PartPublicSchema  # noqa:
from app.schema.part import PartUpdateSchema  # noqa:
from app.schema.part import PartCreateSchema

Faker.seed(0)  # reproducible random

fake = Faker()
fake.add_provider(OptionalProvider)


class PartCreateSchemaFactory(factory.Factory):
    class Meta:
        model = PartCreateSchema

    name = fake.word()
    description = fake.text()
    footprint = fake.bothify(text="SO?-#", letters="PT")
    manufacturer = fake.company()
    mpn = fake.bothify(text="???-####-###-???")
    notes = fake.text()
