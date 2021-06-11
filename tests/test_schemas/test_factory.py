from typing import List

import factory

from app.models.part import PartModel
from tests.factories import PartCreateSchemaFactory


class TestPartFactory:
    def test_new_part_create_schema(self, capsys):
        part = factory.build(dict, FACTORY_CLASS=PartCreateSchemaFactory)
        print(part)
        captured = capsys.readouterr()
        assert part is not None
        assert "'name':" in captured.out

    def test_multi_parts_create_schema(self):
        part = PartCreateSchemaFactory.build_batch(6)
        print(*part)
        assert len(part) == 6
        # assert "'name':" in captured.out

    def test_nanoid_generation(self, part_model_factory):
        part: List[PartModel] = part_model_factory.build_batch(2)
        print(*part)
        assert len(part) == 2
        assert part[0].id != part[1].id
