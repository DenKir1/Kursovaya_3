import pytest

from utils.utils import compare_dates
from utils.utils import format_time
from utils.utils import mask_num
from utils.utils import read_file
from utils.utils import sort_five
from utils.utils import required_str
from utils.utils import exec_tr


@pytest.mark.parametrize('a, b, c', [
    ("2018-09-13T04:43:11.374324", "2018-07-22T07:42:32.953324", True),
("2018-02-13T04:43:11.374324", "2018-07-22T07:42:32.953324", False),
])
def test_compare(a, b, c):
    assert compare_dates(a, b) == c


@pytest.mark.parametrize('d, e', [
    ("2018-09-13T04:43:11.374324", "13.09.2018"),
    ("", None),
])
def test_date(d, e):
    assert format_time(d) == e


@pytest.mark.parametrize('f, g', [
    ("Счет 45735917297559088682", "Счет **8682"),
    ("", None),
    ("Maestro 1913883747791351", "Maestro 1913 88** **** 1351")
])
def test_mask(f, g):
    assert mask_num(f) == g


@pytest.mark.parametrize('i, k, l, m', [
    ("./operation1.json", 7, "", None),

])
def test_read(i, k, l, m):
    assert len(read_file(i)) == k
    assert read_file(l) == m


@pytest.mark.parametrize('o, p', [
    ("./operation1.json", 5, ),

])
def test_sort(o, p):
    assert len(sort_five(read_file(o))) == p


@pytest.mark.parametrize('o, p', [
    ("./operation1.json", 82, ),
])
def test_strreq(o, p):
    assert len(required_str(sort_five(read_file(o))[1])) == p


@pytest.mark.parametrize('t, u', [
    ({"state": "EXECUTED"}, True, ),

])
def test_exec_tr(t, u):
    assert exec_tr(t) == u