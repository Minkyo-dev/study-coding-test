import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(nums1: list[int], nums2: list[int]) -> int:
    min_len = min(len(nums1), len(nums2))

    max_dot_product = -9999999999999999999999999

    from itertools import combinations
    for l in range(min_len):
        # 길이가 l인 부분 집합 구하기
        per1 = list(combinations(nums1, l))
        per2 = list(combinations(nums2, l))
        for p1 in per1:
            if not p1 :
                continue
            for p2 in per2:
                if not p2:
                    continue
                tmp_p = 0
                for _p1, _p2 in zip(p1, p2):
                    tmp_p += (_p1 * _p2)
                if max_dot_product < tmp_p:
                    print("p1, p2", p1, p2)
                    max_dot_product = tmp_p
    return max_dot_product

@profile_time_memory
def othersolution(nums1: list[int], nums2: list[int]) -> int:
    import math
    m, n = len(nums1), len(nums2)
    f = [[-math.inf] * (n + 1) for _ in range(m + 1)]
    for i, x in enumerate(nums1, 1):
        for j, y in enumerate(nums2, 1):
            v = x * y
            f[i][j] = max(f[i - 1][j], f[i][j - 1], max(0, f[i - 1][j - 1]) + v)
    return f[m][n]

if __name__ == "__main__":
    nums1 = [13,-7,12,-15,-7,8,3,-7,-5,13,-15,-8,5,7,-1,3,-11,-12,2,-12]
    nums2 = [-1,13,-4,-2,-13,2,-4,6,-9,13,-8,-3,-9]
    # print(mysolution(nums1, nums2))
    print(othersolution(nums1, nums2))
    