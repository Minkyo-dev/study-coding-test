import pytest
from solution import mysolution, othersolution

args = "N, K, D, expected"
params = [
    pytest.param(10, 2, [3, -2, -4, -9, 0, 3, 7, 13, 8, -3], 21),
    pytest.param(10, 5, [3, -2, -4, -9, 0, 3, 7, 13, 8, -3], 31)
]

@pytest.mark.parametrize(args, params)
def test_mysolution(N, K, D, expected):
    assert mysolution(N, K, D) == expected

@pytest.mark.parametrize(args, params)
def test_othersolution(N, K, D, expected):
    assert othersolution(N, K, D) == expected
    