import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory
from typing import List


@profile_time_memory
def mysolution(nums: List[int], val: int):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
            print(nums)
    print(k)
    return k


@profile_time_memory
def othersolution(nums: List[int], val: int):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    k = 0
    for i in range(len(nums)):
        if (nums[i] != val):
            nums[k] = nums[i]
            k += 1
            print(nums)
    print(k)
    return k


if __name__ == "__main__":
    # nums = [3,2,2,3]
    # val = 3
    # 
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    mysolution(nums, val)
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    othersolution(nums, val)
