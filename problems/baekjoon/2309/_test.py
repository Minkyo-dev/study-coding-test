import pytest
from solution import mysolution, othersolution

args = "dwarfs_ls, expected"
params = [
    pytest.param([20, 7, 23, 19, 10, 15, 25, 8, 13], [7, 8, 10, 13, 19, 20, 23], id="sinario1")
]

@pytest.mark.parametrize(args, params)
def test_mysolution(dwarfs_ls, expected):
    assert mysolution(dwarfs_ls) == expected

@pytest.mark.parametrize(args, params)
def test_othersolution(dwarfs_ls, expected):
    assert othersolution(dwarfs_ls) == expected
