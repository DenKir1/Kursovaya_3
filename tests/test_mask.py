import pytest
from utils.mask_number import *

@pytest.mark.parametrize('a, b', [
    ("Счет 45735917297559088682", "Счет **8682"),
    ("", None),
    ("Maestro 1913883747791351", "Maestro 1913 88** **** 1351")
])
def test_mask(a, b):
    assert mask_num(a) == b