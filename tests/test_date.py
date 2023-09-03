import pytest
from utils.date_from import *

@pytest.mark.parametrize('a, b', [
    ("2018-09-13T04:43:11.374324", "13.09.2018"),
("", None),
])
def test_date(a, b):
    assert format_time(a) == b