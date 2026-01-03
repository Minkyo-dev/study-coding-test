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

    for i in range(N):
        r_idx = i
        case_sum = 0
        if seq_ls[i] == M:
            case_cnt += 1
            print("처음부터 완료", i, r_idx)
            continue
        else:
            while r_idx <= N:
                if case_sum == M:
                    case_cnt += 1
                    print("while 완료", i, r_idx)
                    break
                elif case_sum > M:
                    print("while 커짐", i, r_idx)
                    break
                case_sum += seq_ls[r_idx]
                print("while 인덱스 추가", case_sum, i, r_idx)
                r_idx += 1
    return case_cnt


@profile_time_memory
def othersolution(N, M, seq):
    start =0
    end = 0
    sum = seq[0]

    sount = 0
    while True:
        # 현재 구간 합이 M인지 확인
        if sum == M:
            count += 1
        # 구간 업데이트
        if (sum>= M):
            start+= 1
            sum -= A[start-1]
    pass

if __name__ == "__main__":
    N = 4
    M = 2
    seq = "1 1 1 1"
    print(mysolution(N, M, seq))
    # othersolution()
