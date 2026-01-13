import sys
import os
from typing import List
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(N: int, p_ls: List[int], del_n: int) -> int:
    """
    Args:
        N: 노드의 개수
        p_ls: 부모 노드 번호 리스트
        del_n: 삭제할 노드 번호
    Return:
        int : 남은 리프노드 개수
    Result:
        틀림
        왜 틀렸는지 파악 안됨
    """
    c_dict = {i: [] for i in range(N)}

    # 자식 트리 만들기
    for i in range(N):
        if p_ls[i] == -1:
            continue
        else:
            c_dict[p_ls[i]].append(i)

    # 삭제할 노드 지우기
    del_n_child = c_dict[del_n]
    while True :
        if len(del_n_child) == 0:
            del c_dict[del_n]
            break
        del_n_ls = del_n_child.copy()
        del_n_child = []
        for n in del_n_ls:
            del_n_child.extend(c_dict[n])
            del c_dict[n]

    print(c_dict)
    ans = 0
    for k in c_dict.keys():
        if len(c_dict[k]) == 0:
            ans += 1
    print(ans)
    return ans

@profile_time_memory
def othersolution(N: int, p_ls: List[int], del_n: int) -> int:
    # 루트 노드 찾기
    for i in range(N):
        if p_ls[i] == -1 :
            root = i
            break

    # 사라지는 노드 탐색
    black = [0] * N
    for i in range(N):
        u = i
        while True:
            if u == del_n:
                black[i] = 1
                break
            if u == root:
                break
            # 부모노드
            u = p_ls[u]
    
    # 자식이 있는 노드들 색칠
    red = [0] * N
    for i in range(N):
        if black[i] == 1:
            continue
        
        if i == root:
            continue

        red[p_ls[i]] = 1
    
    ans = 0
    for i in range(N):
        if black[i] == 1 or red[i] == 1:
            continue
        ans += 1
    return ans

if __name__ == "__main__":
    N = 5
    p_ls = [-1, 0, 0, 1, 1]
    del_n = 2
    print("1st", mysolution(N, p_ls, del_n))
    
    N = 5
    p_ls = [-1, 0, 0, 1, 1]
    del_n = 1
    print("2nd", mysolution(N, p_ls, del_n))

    N = 5
    p_ls = [-1, 0, 0, 1, 1]
    del_n = 0
    print("3rd", mysolution(N, p_ls, del_n))

    N = 9
    p_ls = [-1, 0, 0, 2, 2, 4, 4, 6, 6]
    del_n = 4
    print("4th", mysolution(N, p_ls, del_n))
    
    othersolution()
    