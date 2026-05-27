import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory
from typing import List


@profile_time_memory
def mysolution(nums: List[int]) -> int:
    # dynamic programing, greedy
    def is_over_end(cur_idx, step, end_idx):
        return end_idx < (cur_idx + step)
    
    step_cnt = 0
    def recursive_exploring(target_list):
        target_len = len(target_list)
        for cur_idx, n in enumerate(target_list):
            for step in range(1, n+1):
                if is_over_end(cur_idx, step, target_len):
                    return step_cnt
                else:
                    recursive_exploring(target_list[cur_idx:])

    recursive_exploring(nums)




@profile_time_memory
def othersolution(nums: List[int]) -> int:
    jump_count = 0
    cur_jump_end = 0
    farthest_reachable = 0

    for i in range(len(nums) - 1):
        # Update the farthest index we can reach from current position
        farthest_reachable = max(farthest_reachable, i + nums[i])

        # If we've reached the end of the current jump's range
        if i == cur_jump_end:
            # We must make another jump
            jump_count += 1
            # Update the range of the next jump to the farthest we can reach
            cur_jump_end = farthest_reachable
    return jump_count


if __name__ == "__main__":
    nums = [2,3,1,1,4]
    # print(mysolution(nums))
    print(othersolution(nums))
