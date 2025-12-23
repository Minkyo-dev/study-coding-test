import pytest

from solution import mysolution, othersolution1

@pytest.mark.parametrize(
    "N, budget_requests, total_budget, expected",
    [
        pytest.param(4, [120, 110, 140, 150], 485, 127, id="sinario1"),
        pytest.param(5, [70, 80, 30, 40, 100], 450, 100, id="sinario2"),
        ],
)
def test(N, budget_requests, total_budget, expected):
    assert mysolution(N, budget_requests, total_budget) == expected

@pytest.mark.parametrize(
    "N, budget_requests, total_budget, expected",
    [
        pytest.param(4, [120, 110, 140, 150], 485, 127, id="sinario1"),
        pytest.param(5, [70, 80, 30, 40, 100], 450, 100, id="sinario2"),
        ],
)
def test2(N, budget_requests, total_budget, expected):
    assert othersolution1(N, budget_requests, total_budget) == expected
