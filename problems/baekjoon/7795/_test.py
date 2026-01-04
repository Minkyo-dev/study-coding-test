import pytest
from solution import mysolution, othersolution

args = "expected"
params = [
    pytest.param(2, [{
        "A_B_cnt" : "5 3",
        "A" : "8 1 7 3 1",
        "B" : "3 6 1"
    }, {
        "A_B_cnt" : "3 4",
        "A" : "2 13 7",
        "B" : "103 11 290 215"
    }], [7, 1], id="sinario1")
]

@pytest.mark.parametrize(args, params)
def test_mysolution(T, case, expected):
    assert mysolution(T, case) == expected

@pytest.mark.parametrize(args, params)
def test_othersolution(T, case, expected):
    assert othersolution(T, case) == expected
    