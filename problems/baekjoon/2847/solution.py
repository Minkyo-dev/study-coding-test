import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(N: int, levels: list[int]) -> int:
    """
    Args:
        N (int): 게임 레벨 횟수
        levels (list[int]) : 각 레벨별 점수
    """
    highest_point = levels[-1]
    minus_cnt = 0
    for i in range(N-1):
        lp = levels[N-i-2]
        while True:
            if lp < highest_point:
                highest_point = lp
                break
            minus_cnt += 1
            lp -= 1
    return minus_cnt
    

@profile_time_memory
def othersolution(N: int, levels: list[int]) -> int:
    count = 0
    for i in range(N - 2, -1, -1):
        if levels[i] >= levels[i + 1]:
            count += levels[i] - (levels[i + 1] - 1)
            levels[i] = levels[i + 1] - 1
    return count

if __name__ == "__main__":
    N = 4
    levels = [
        5,3,7,5
    ]
    mysolution(N, levels)
    othersolution(N ,levels)
    