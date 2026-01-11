import pytest
from solution import mysolution, othersolution

args = "N, levels, expected"
params = [
    pytest.param(3, [5,5,5], 3),
    pytest.param(4, [5,3,7,5], 6)
]

@pytest.mark.parametrize(args, params)
def test_mysolution(N, levels, expected):
    assert mysolution(N, levels) == expected

@pytest.mark.parametrize(args, params)
def test_othersolution(N, levels, expected):
    assert othersolution(N, levels) == expected
    