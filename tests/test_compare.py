import pytest
from utils.compare_date import *

@pytest.mark.parametrize('a, b, c', [
    ("2018-09-13T04:43:11.374324", "2018-07-22T07:42:32.953324", True),
("2018-02-13T04:43:11.374324", "2018-07-22T07:42:32.953324", False),
])
def test_compare(a, b, c):
    assert compare_dates(a, b) == c