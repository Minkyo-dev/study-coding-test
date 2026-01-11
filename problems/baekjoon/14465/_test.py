import pytest
from solution import mysolution, othersolution

args = "N, K, B, C, expected"
params = [
    pytest.param(10, 6, 5, [2,10,1,5,9], 1)
]

@pytest.mark.parametrize(args, params)
def test_mysolution(N, K, B, C, expected):
    assert mysolution(N, K, B, C) == expected

@pytest.mark.parametrize(args, params)
def test_othersolution(N, K, B, C, expected):
    assert othersolution(N, K, B, C) == expected
    