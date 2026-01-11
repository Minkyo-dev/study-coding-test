import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(N: int, K: int, D: list[int]):
    """
    Args:
        N : 온도를 측정한 전체 날짜의 수
        K : 합을 구하기 위한 연속적인 날짜의 수
        D : 매일 측정한 온도를 나타내는 N개의 정수 리스트
    실행 시간: 0.058 ms
    Python 메모리 피크: 0.00 MB
    RSS 증가량: 0.12 MB
    """
    psum = []
    # K 간격의 sum 구하기
    for i in range(N-K+1):
        psum.append(sum(D[i:i+K]))
    # print(psum)
    return max(psum)

@profile_time_memory
def othersolution(N: int, K: int, D: list[int]):
    """
    실행 시간: 0.022 ms
    Python 메모리 피크: 0.00 MB
    RSS 증가량: 0.00 MB
    """
    # 누적합 (prefix sum) 구하기
    psum = [0] * N
    psum[0] = D[0]
    for i in range(1, N):
        psum[i] = psum[i-1] + D[i]
    # print(psum)

    # 연속된 K일 온도 합
    temp_sum = []
    for i in range(0, N - K + 1):
        if i == 0:
            sum = psum[i + K - 1]
        else:
            sum = psum[i + K - 1] - psum[i - 1]
        temp_sum.append(sum)
    # print(temp_sum)
    return max(temp_sum)

if __name__ == "__main__":
    N = 10
    K = 2
    D = [3, -2, -4, -9, 0, 3, 7, 13, 8, -3]
    print(mysolution(N, K, D))
    print(othersolution(N, K, D))
    