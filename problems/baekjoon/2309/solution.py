import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(dwarfs_ls: list[int]) -> list[int]:
    from itertools import combinations

    seven_dwarfs_ls = combinations(dwarfs_ls, 7)
    answer_ls = []
    for seven_dwarfs in seven_dwarfs_ls:
        if sum(seven_dwarfs) == 100:
            answer_ls.append(seven_dwarfs)
            break
    return sorted(answer_ls[0])

@profile_time_memory
def othersolution(dwarfs_ls: list[int]) -> list[int]:
    from itertools import combinations
    answer = []
    for a in combinations(dwarfs_ls, 7):
        if sum(a) == 100 :
            a = list(a)
            a.sort()
            for x in a:
                answer.append(x)
            break
    return answer



if __name__ == "__main__":
    dwarfs_ls = [20, 7, 23, 19, 10, 15, 25, 8, 13]
    print(mysolution(dwarfs_ls))
    othersolution()
