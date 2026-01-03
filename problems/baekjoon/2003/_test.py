import pytest
from solution import mysolution, othersolution

args = "N, M, seq, expected"
params = [
    pytest.param(4, 2, "1 1 1 1", 3, id="sinario1"),
    pytest.param(10, 5, "1 2 3 4 2 5 3 1 1 2", 3, id="sinario2"),
]

@pytest.mark.parametrize(args, params)
def test_mysolution(N, M, seq, expected):
    assert mysolution(N, M, seq) == expected

@pytest.mark.parametrize(args, params)
def test_othersolution(N, M, seq, expected):
    assert othersolution(N, M, seq) == expected
