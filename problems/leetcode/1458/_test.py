import pytest
from solution import mysolution, othersolution

args = "nums1, nums2, expected"
params = [
    pytest.param([2,1,-2,5], [3,0,-6], 18),
    pytest.param([3,-2], [2,-6,7], 21),
    pytest.param([-1,-1], [1,1], -1),
    pytest.param([13,-7,12,-15,-7,8,3,-7,-5,13,-15,-8,5,7,-1,3,-11,-12,2,-12], [-1,13,-4,-2,-13,2,-4,6,-9,13,-8,-3,-9], 972),
]

# @pytest.mark.parametrize(args, params)
# def test_mysolution(nums1, nums2, expected):
#     assert mysolution(nums1, nums2) == expected

@pytest.mark.parametrize(args, params)
def test_othersolution(nums1, nums2, expected):
    assert othersolution(nums1, nums2) == expected
    