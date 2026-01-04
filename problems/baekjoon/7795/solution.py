import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(T: int, case: list[dict]):
    """
    Args:
        T : 테스트 케이스의 개수
        case : 케이스별 입력값 
            ex : [{
                "A_B_cnt" : "5 3",
                "A" : "8 1 7 3 1",
                "B" : "3 6 1"
            }, ...]
    """
    res_ls = []
    for t in range(T):
        c: dict = case[t]
        A_cnt, B_cnt = list(map(int, c["A_B_cnt"].split()))
        A = list(map(int, c["A"].split()))
        B = list(map(int, c["B"].split()))

        can_eat_cnt = 0
        for a_idx in range(A_cnt):
            a = A[a_idx]
            for b_idx in range(B_cnt):
                b = B[b_idx]
                if (a > b) :
                    can_eat_cnt += 1
        
        res_ls.append(can_eat_cnt)
    
    return res_ls


@profile_time_memory
def othersolution(T: int, case: list[dict]):
    res_ls = []
    for t in range(T):
        c: dict = case[t]
        N, M = list(map(int, c["A_B_cnt"].split()))
        A = list(map(int, c["A"].split()))
        B = list(map(int, c["B"].split()))

        A = sorted(A)
        B = sorted(B)
        
        main = 0
        sub = 0
        count = 0

        while main < N:
            if sub == M:
                count += sub
                main += 1
            else:
                if A[main] > B[sub]:
                    sub += 1
                else:
                    count += sub
                    main += 1
        res_ls.append(count)
    
    return res_ls

if __name__ == "__main__":
    T = 2
    case = [{
        "A_B_cnt" : "5 3",
        "A" : "8 1 7 3 1",
        "B" : "3 6 1"
    }, {
        "A_B_cnt" : "3 4",
        "A" : "2 13 7",
        "B" : "103 11 290 215"
    }]
    print(mysolution(T, case))
    print(othersolution(T, case))
    