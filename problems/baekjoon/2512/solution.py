# baekjoon 2512번 예산
def mysolution(N: int, budget_requests: list[int], total_budget: int) -> int:
    """
    args:
      N : 지방의 수
      budget_requests : 예산 요청 금액 리스트
      total_budget : 전체 예산
    """
    cal_tot_budget = sum(budget_requests)
    limit_budget = max(budget_requests)

    if cal_tot_budget <= total_budget:
        return limit_budget

    while True:
        new_tot_budget = 0
        limit_budget -= 1

        for budget in budget_requests:
            if budget <= limit_budget:
                new_tot_budget += budget
            else:
                new_tot_budget += limit_budget

        if new_tot_budget <= total_budget:
            return limit_budget

def othersolution1(N: int, budget_requests: list[int], total_budget: int) -> int:
    left = 0
    right = max(budget_requests)
    answer  = -1

    while left <= right :
        middle = (left + right) // 2

        sum = 0
        for i in range(N):
            sum += min(middle, budget_requests[i])

        if sum <= total_budget:
            answer = middle
            left = middle + 1
        else :
            right = middle - 1
    return answer

if __name__ == "__main__":
    res = mysolution(4, [120, 110, 140, 150], 485)
    print(res)





