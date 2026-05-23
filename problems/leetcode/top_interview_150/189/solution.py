import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory
from typing import List


@profile_time_memory
def mysolution(nums: List, k: int) -> List[int]:
    for _ in range(3):
        last_int = nums.pop(-1)
        nums = [last_int] + nums
        print(nums)
    print(nums)
    return nums


@profile_time_memory
def othersolution(nums: List, k: int) -> List[int]:
    n = len(nums)
    k %= n

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # 1. Reverse the entire array
    reverse(0, n - 1)
    # 2. Reverse the first k elements
    reverse(0, k - 1)
    # 3. Reverse the remaining n - k elements
    reverse(k, n - 1)
    print(nums)
    return nums


if __name__ == "__main__":
    # nums = [1,2,3,4,5,6,7]
    # k = 3
    nums = [-1,-100,3,99]
    k = 2
    mysolution(nums, k)
    othersolution(nums, k)
