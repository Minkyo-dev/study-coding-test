import sys
import os
from typing import Optional
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

@profile_time_memory
def mysolution(root: Optional[TreeNode]):
    # 1, 2, 4, 8
    level = 1
    level_node_cnt = 1
    start_idx = 0
    end_idx = 1

    biggest_level = -1
    level_sum = -1

    _root = []
    for i in range(len(root)):
        if not root[i]:
            _root.append(0)
        else:
            _root.append(root[i])

    while True:
        if len(_root) < end_idx -1 :
            break

        # 해당 층의 sum 구하기
        tmp_sum = sum(_root[start_idx:end_idx])

        # sum 비교하기;
        if level_sum < tmp_sum:
            level_sum = tmp_sum
            biggest_level = level

        # 다음 레벨로 넘어가기
        level += 1
        start_idx += level_node_cnt
        level_node_cnt *= 2
        end_idx += level_node_cnt

    return biggest_level

@profile_time_memory
def othersolution():
    pass

if __name__ == "__main__":
    root = [1,7,0,7,-8, None, None]
    print(mysolution(root))
    othersolution()
    