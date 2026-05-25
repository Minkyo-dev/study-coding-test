import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory
from typing import List


@profile_time_memory
def mysolution(nums: List[int]) -> bool:
    if len(nums) == 1:
        return True
    last_idx = len(nums) - 1
    for idx, n in enumerate(nums):
        if n == 0:
            return False
        if (n + idx) >= last_idx:
            return True
    return False


@profile_time_memory
def othersolution(nums: List[int]) -> bool:
    # Greedy - start at end
    # https://www.youtube.com/watch?v=PfGypLRcoVA

    n = len(nums)
    target_goal = n - 1

    for i in range(n-1, -1, -1) :
        max_jump = nums[i]
        if max_jump + i >= target_goal :
            target_goal = i
    return target_goal == 0


if __name__ == "__main__":
    # nums = [2,3,1,1,4]
    # nums = [3,2,1,0,4]
    # nums = [0]
    # nums = [2,0,0]
    # nums = [2,5,0,0]
    nums = [3,0,8,2,0,0,1]
    print(mysolution(nums))
    print(othersolution(nums))
