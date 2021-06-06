import factory

from tests.factories import PartCreateSchemaFactory


def test_new_part_create_schema(capsys):
    part = factory.build(dict, FACTORY_CLASS=PartCreateSchemaFactory)
    print(f"{part}")
    captured = capsys.readouterr()
    assert part is not None
    assert "'name':" in captured.out
