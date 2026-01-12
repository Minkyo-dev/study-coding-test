import pytest
from solution import mysolution, othersolution

args = "points, expected"
params = [
    pytest.param([[1,1],[3,4],[-1,0]], 7),
    pytest.param([[3,2],[-2,2]], 5),
]

@pytest.mark.parametrize(args, params)
def test_mysolution(points, expected):
    assert mysolution(points) == expected

@pytest.mark.parametrize(args, params)
def test_othersolution(points, expected):
    assert othersolution(points) == expected
    