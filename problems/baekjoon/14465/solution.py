import sys
import os
from typing import List
import math
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(N: int, K: int, B: int, C: List[int]) -> int:
    """
    Args:
        N: 횡단보도 개수 1~N
        K: 연속된 횡단보도 개수
        B: 망가진 횡단보도 개수
        C: 망가진 횡단보도 번호 리스트

    결과 :
        누적합 만들기 전 : 시간 초과 됨
        실행 시간: 0.415 ms
        Python 메모리 피크: 0.00 MB
        RSS 증가량: 0.12 MB

        누적합 만든 후 : 
        실행 시간: 0.119 ms
        Python 메모리 피크: 0.00 MB
        RSS 증가량: 0.12 MB
    """
    # b_ls = [0 if i in C else 1 for i in range(1, N+1) ]
    # print(b_ls)

    # min_fix = math.inf

    # for i in range(N - K + 1):
    #     print(b_ls[i: i+K])
    #     fix_c = K - sum(b_ls[i: i+K])
    #     print(fix_c)
    #     if fix_c < min_fix :
    #         min_fix = fix_c
    # print("min_fix", min_fix)
    # return min_fix

    b_ls = [1 if i in C else 0 for i in range(1, N+1) ]

    # 누적합 리스트 만들기
    psum = []
    for i in range(N):
        if i == 0:
            psum.append(b_ls[i])
        else:
            psum.append(psum[i-1] + b_ls[i])
    print(psum)

    need_fix_ls = []
    for i in range(N - K) :
        need_fix_ls.append(psum[i+K] - psum[i])
    print(min(need_fix_ls))
    return min(need_fix_ls)


@profile_time_memory
def othersolution(N: int, K: int, B: int, C: List[int]) -> int:
    check = [0] * N

    for i in range(B):
        id = C[i]
        check[id - 1] = 1
    print("check", check)
    
    psum = [0] * N
    psum[0] = check[0]
    for i in range(1, N):
        psum[i] = psum[i - 1] + check[i]
    print("psum", psum)

    need = []
    for i in range(0, N - K + 1):
        if i == 0:
            num = psum[i + K - 1]
        else:
            num = psum[i + K - 1] - psum[i - 1]
        need.append(num)
    print("need", min(need))
    return min(need)

if __name__ == "__main__":
    N = 10
    K = 6
    B = 5
    C = [2,10,1,5,9]
    mysolution(N, K, B, C)
    othersolution(N, K, B, C)
    