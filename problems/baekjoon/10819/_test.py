import pytest
from solution import mysolution, othersolution

args = "N, A, expected"
params = [
    pytest.param(6, [20, 1, 15, 8, 4, 10], 62, id="sinario1")
]

@pytest.mark.parametrize(args, params)
def test_mysolution(N, A, expected):
    assert mysolution(N, A) == expected

@pytest.mark.parametrize(args, params)
def test_othersolution(N, A, expected):
    assert othersolution(N, A) == expected
