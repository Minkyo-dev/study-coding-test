import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory
from typing import List


@profile_time_memory
def mysolution(nums: List[int]):
    k = 1
    for i in range(len(nums)):
        if nums[i] > nums[k-1] :
            nums[k] = nums[i]
            k += 1
        print(nums)
        print("i: {}, k: {}".format(i, k))
    print(k)




@profile_time_memory
def othersolution():
    pass


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    mysolution(nums)
    othersolution()
