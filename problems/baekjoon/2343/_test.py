import pytest

from solution import mysolution, othersolution1

args = "N, M, lesson, expected"
params = [
    pytest.param(9, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], 17, id="sinario1"),
]

@pytest.mark.parametrize(args, params)
def test(N, M, lesson, expected):
    assert othersolution1(N, M, lesson) == expected
