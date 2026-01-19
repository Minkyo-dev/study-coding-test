import sys
import os
from typing import List
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(mat: List[List[int]], threshold: int) -> int:
    """
    args:
      mat : 행렬
      threshold : 임계값
    return:
      answer : 정사각형의 최대 한 변의 길이
    """
    pass


@profile_time_memory
def othersolution(mat: List[List[int]], threshold: int) -> int:
    m, n = len(mat), len(mat[0])
    P = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            P[i][j] = (
                P[i - 1][j]
                + P[i][j - 1]
                - P[i - 1][j - 1]
                + mat[i - 1][j - 1]
            )
            print(P)

    def getRect(x1, y1, x2, y2):
        return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]

    # binary search for side length
    l, r, ans = 1, min(m, n), 0
    while l <= r:
        mid = (l + r) // 2
        find = any(
            getRect(i, j, i + mid - 1, j + mid - 1) <= threshold
            for i in range(1, m - mid + 2)
            for j in range(1, n - mid + 2)
        )
        if find :
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    print(ans)
    return ans

if __name__ == "__main__":
    mat = [
    [1,1,3,2,4,3,2],
    [1,1,3,2,4,3,2],
    [1,1,3,2,4,3,2]
    ]
    threshold = 4
    mysolution(mat, threshold)
    othersolution(mat, threshold)
