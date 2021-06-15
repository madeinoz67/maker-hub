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
