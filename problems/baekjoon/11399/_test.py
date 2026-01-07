import pytest
from solution import mysolution, othersolution

args = "N, P, expected"
params = [
    pytest.param(5, [3, 1, 4, 3, 2], 32, id="sinario1")
]

@pytest.mark.parametrize(args, params)
def test_mysolution(N, P, expected):
    assert mysolution(N, P) == expected

@pytest.mark.parametrize(args, params)
def test_othersolution(N, P, expected):
    assert othersolution(N, P) == expected
