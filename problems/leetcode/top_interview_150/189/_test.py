import pytest
from solution import mysolution, othersolution

args = "nums, k, expected"
params = [
    pytest.param([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
    pytest.param([-1,-100,3,99], 2, [3,99,-1,-100])
]


@pytest.mark.parametrize(args, params)
def test_mysolution(nums, k, expected):
    assert mysolution(nums, k) == expected


@pytest.mark.parametrize(args, params)
def test_othersolution(nums, k, expected):
    assert othersolution(nums, k) == expected
