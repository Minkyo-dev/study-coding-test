import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(nums: list[int]) -> int:
    if nums == sorted(nums):
        print("sorted")
    else:
        print(nums)

@profile_time_memory
def othersolution():
    pass

if __name__ == "__main__":
    nums = [5,2,3,1]
    mysolution(nums)
    othersolution()
    