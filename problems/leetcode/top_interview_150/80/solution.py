import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory
from typing import List


@profile_time_memory
def mysolution(nums: List[int]) -> int:
    n = 0
    m = 1
    while m < len(nums):
        if nums[n] == nums[m] and m - n >= 2:
            n = m
            m += 1
        elif nums[n] != nums[m]:
            nums[n] = nums[m]
            m += 1
        else:
            m += 1
        print(f"{nums=}, {n=}, {m=}")
    return n + 1



@profile_time_memory
def othersolution(nums: List[int]) -> int:
    writer = 1
    count = 1
    m = len(nums)
    for i in range(1, m):
        print(f"{nums=}, {writer=}, {i=}, {count=}")
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1
        
        if count <= 2:
            nums[writer] = nums[i]
            writer += 1

    return writer


if __name__ == "__main__":
    # nums = [1,1,1,2,2,3]/
    nums = [0,0,1,1,1,1,2,3,3]
    mysolution(nums)
    nums = [0,0,1,1,1,1,2,3,3]
    othersolution(nums)
