import pytest
from solution import mysolution, othersolution

args = "nums, expected"
params = [
    pytest.param([2,3,5,7], [-1,1,4,3]),
    pytest.param([11,13,31], [9,12,15])
]

@pytest.mark.parametrize(args, params)
def test_mysolution(nums, expected):
    assert mysolution(nums) == expected

# @pytest.mark.parametrize(args, params)
# def test_othersolution(expected):
#     assert othersolution() == expected
    