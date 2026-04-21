import pytest
from solution import mysolution, othersolution

args = "m, n, nums1, nums2, expected"
params = [
    pytest.param(3, 3, [1,2,3,0,0,0], [2,5,6], [1,2,2,3,5,6], id="example1"),
    pytest.param(1, 0, [1], [], [1], id="example2"),
    pytest.param(0, 1, [0], [1], [1], id="example3"),
]


@pytest.mark.parametrize(args, params)
def test_mysolution(m, n, nums1, nums2, expected):
    assert mysolution(m, n, nums1, nums2) == expected


# @pytest.mark.parametrize(args, params)
# def test_othersolution(expected):
#     assert othersolution() == expected
