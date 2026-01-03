import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(N:int, M:int, seq:str):
    """
    args:
        N : 수열의 개수
        M : 합의 결과
        seq: 수열 문자열 ex. '1 1 1 1'
    """
    seq_ls = list(map(int, seq.split()))
    case_cnt = 0

    for start_idx in range(N):
        for end_idx in range(N+1):
            if start_idx > end_idx :
                continue
            sum_seq = sum(seq_ls[start_idx:end_idx])
            if sum_seq == M :
                case_cnt += 1
                continue

    return case_cnt



@profile_time_memory
def othersolution(N:int, M:int, seq:str):
    start = 0  # 시작점
    end = 0  # 끝점
    A = list(map(int, seq.split()))
    sum = A[0]  # 구간 합

    count = 0
    while True:
        # 현재 구간 합이 M인지 확인
        if sum == M:
            count += 1

        # 구간 업데이트
        if (sum>= M):
            start+= 1
            sum -= A[start-1]
        else:
            if end == N-1:
                break

            end += 1
            sum += A[end]
    return count

if __name__ == "__main__":
    N = 4
    M = 2
    seq = "1 1 1 1"
    print(mysolution(N, M, seq))
    print(othersolution(N, M, seq))
    N = 10
    M = 5
    seq = "1 2 3 4 2 5 3 1 1 2"
    print(mysolution(N, M, seq))
    print(othersolution(N, M, seq))

