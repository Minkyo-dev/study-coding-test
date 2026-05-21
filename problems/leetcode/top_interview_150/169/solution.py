import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory
from typing import List

@profile_time_memory
def mysolution(nums: List[int]) -> int:
    count_dict = {}
    _standard = len(nums) / 2
    for e in nums:
        if e in count_dict.keys():
            count_dict[e] += 1
        else:
            count_dict[e] = 1

    return next(k for k, v in count_dict.items() if v > _standard)


@profile_time_memory
def othersolution(nums: List[int]) -> int:
    # First pass: Find candidate
    count = 0
    candidate = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1
        print(f"num: {num}, candidate: {candidate}, count: {count}")

    # Second pass: Verify (only needed if majority element might not exist)
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None  # No majority element exists


if __name__ == "__main__":
    nums = [1,1,1,2,2,2,2]
    print(mysolution(nums))
    print(othersolution(nums))
