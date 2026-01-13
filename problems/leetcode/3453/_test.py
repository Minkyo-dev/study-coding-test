import pytest
from solution import mysolution, othersolution

args = "expected"
params = []

@pytest.mark.parametrize(args, params)
def test_mysolution(expected):
    assert mysolution() == expected

@pytest.mark.parametrize(args, params)
def test_othersolution(expected):
    assert othersolution() == expected
    