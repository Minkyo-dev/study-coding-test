import pytest
from solution import mysolution, othersolution

args = "N, p_ls, del_n, expected"
params = [
    pytest.param(5, [-1, 0, 0, 1, 1], 2, 2),
    pytest.param(5, [-1, 0, 0, 1, 1], 1, 1),
    pytest.param(5, [-1, 0, 0, 1, 1], 0, 0),
    pytest.param(9, [-1, 0, 0, 2, 2, 4, 4, 6, 6], 4, 2),
]

@pytest.mark.parametrize(args, params)
def test_mysolution(N, p_ls, del_n, expected):
    assert mysolution(N, p_ls, del_n) == expected

@pytest.mark.parametrize(args, params)
def test_othersolution(N, p_ls, del_n, expected):
    assert othersolution(N, p_ls, del_n) == expected
    