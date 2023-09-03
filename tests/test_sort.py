import pytest
from utils.sort_newest import *
from utils.read_json import *

@pytest.mark.parametrize('a, b', [
    ("tests/operation1.json", 5, ),

])
def test_sort(a, b):
    assert len(sort_five(read_file(a))) == b
