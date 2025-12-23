import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(arr_size: str, arr_ls: list[str]) -> str:
    """
    args:
      arr_size : 배열 A의 크기 N, 배열 B의 크기 M
      arr_ls : 배열 A의 내용, 배열 B의 내용
    """
    a_size, b_size = arr_size.split()
    a_ls = arr_ls[0].split()
    b_ls = arr_ls[1].split()
    a_ls.extend(b_ls)
    merged_ls = sorted(list(set(a_ls)))
    return " ".join(merged_ls)

@profile_time_memory
def othersolution(arr_size: str, arr_ls: list[str]) -> str:
    N, M = map(int, arr_size.split())
    A = list(map(int, arr_ls[0].split()))
    B = list(map(int, arr_ls[1].split()))
    C = []

    posi_a = 0
    posi_b = 0
    while posi_a < N and posi_b < M:
        candidate1 = A[posi_a]
        candidate2 = B[posi_b]

        if candidate1 < candidate2:
            C.append(candidate1)
            posi_a += 1
        else:
            C.append(candidate2)
            posi_b += 1

    if posi_a != N :
        C.extend(A[posi_a:])
    if posi_b != M :
        C.extend(B[posi_b:])

    return " ".join(map(str, C))

if __name__ == "__main__":
    arr_size = "2 2"
    arr_ls = ["3 5", "2 9"]
    res = mysolution(arr_size, arr_ls)
    print(res)
    res = othersolution(arr_size, arr_ls)
    print(res)
