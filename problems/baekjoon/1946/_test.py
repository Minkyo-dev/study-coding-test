import pytest
from solution import mysolution, othersolution

args = "test_cnt, test_cases, expected"
params = [
    pytest.param(2, [(5, [(3, 2),(1, 4),(4, 1),(2, 3),(5, 5)]), (7, [(3, 6),(7, 3),(4, 2),(1, 4),(5, 7),(2, 5),(6, 1),])], [4,3])
]

@pytest.mark.parametrize(args, params)
def test(test_cnt, test_cases, expected):
    assert mysolution(test_cnt, test_cases) == expected
    assert othersolution(test_cnt, test_cases) == expected
