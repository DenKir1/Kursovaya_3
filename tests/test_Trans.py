import pytest
from utils.Transaction import *
from utils.read_json import *

path = "tests/operation1.json"
aa = read_file(path)
tra1 = Transaction(*aa[0].values())
tra2 = Transaction(*aa[1].values())

@pytest.fixture()
def tra(trans):
    return trans

def test_tran_newest():
    assert tra1.newest_than(tra2) == True
    assert tra2.newest_than(tra1) == False

def test_exec():
    assert tra1.exec_tr() == True

def test_repr():
    assert print(tra1) == None