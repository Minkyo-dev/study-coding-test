import sys
import os
from typing import List
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(nums: List[int]):
    """
    Args:
        nums: 소수로 이루어진 정수 배열
    """
    ans_ls = list()

    def get_or_ans_between_two_num(target) :
        num_ls = list(range(1, target))
        ans_num = -1
        for i in num_ls:
            if (i|i+1) == target:
                ans_num = i
                break
        return ans_num
            
    for t in nums:
        ans_ls.append(get_or_ans_between_two_num(t))
    print(ans_ls)
    return ans_ls


@profile_time_memory
def othersolution(nums):
    for i in range(len(nums)):
        res = -1
        d = 1
        while (nums[i] & d) != 0:
            res = nums[i] - d
            d <<= 1
        nums[i] = res

    print(nums)
    return nums

if __name__ == "__main__":
    nums = [2,3,5,7]
    mysolution(nums)
    othersolution(nums)
    nums = [11,13,31]
    mysolution(nums)
    othersolution(nums)
    