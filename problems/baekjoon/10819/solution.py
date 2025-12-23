import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(N: int, A: list[int]) -> int:
    """
    args:
      N : 배열 A의 크기
      A : 배열
    """
    from itertools import permutations
    per_ls = permutations(A, N)

    max_value = -1
    for per in per_ls:
        print(per)
        per_sum = 0
        for idx in range(len(per)-1):
            per_sum += abs(per[idx] - per[idx+1])
        if per_sum > max_value:
            max_value = per_sum
    return max_value

@profile_time_memory
def othersolution(N: int, A: list[int]) -> int:
    from itertools import permutations

    max_diff_sum = 0
    for a in permutations(A, N):
        diff_sum = 0
        for i in range(N - 1):
            diff_sum += abs(a[i] - a[i+1])
        max_diff_sum = max(max_diff_sum, diff_sum)
    return max_diff_sum


if __name__ == "__main__":
    N = 6
    A = [20, 1, 15, 8, 4, 10]
    res = mysolution(N, A)
    print(res)
    othersolution()
