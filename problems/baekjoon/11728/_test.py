import pytest
from solution import mysolution, othersolution

args = "arr_size, arr_ls, expected"
params = [
    pytest.param("2 2", ["3 5", "2 9"], "2 3 5 9", id="sinario1"),
    pytest.param("2 1", ["4 7", "1"], "1 4 7", id="sinario2"),
    pytest.param("4 3", ["2 3 5 9", "1 4 7"], "1 2 3 4 5 7 9", id="sinario3"),
]

@pytest.mark.parametrize(args, params)
def test_mysolution(arr_size, arr_ls, expected):
    assert mysolution(arr_size, arr_ls) == expected

@pytest.mark.parametrize(args, params)
def test_othersolution(arr_size, arr_ls, expected):
    assert othersolution(arr_size, arr_ls) == expected
