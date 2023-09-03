import pytest
from utils.read_json import *

@pytest.mark.parametrize('a, b, c, d', [
    ("tests/operation1.json", 3, "", None),

])
def test_read(a, b, c, d):
    assert len(read_file(a)) == b
    assert read_file(c) == d