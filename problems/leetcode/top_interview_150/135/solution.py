import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory
from typing import List


@profile_time_memory
def mysolution(ratings: List[int]) -> int:
    n = len(ratings)
    res = [1] * n
    for i in range(1, n):
        if ratings[i - 1] < ratings[i]:
            res[i] = res[i - 1] + 1
        elif ratings[i - 1] > ratings[i] :
            p = i - 1
            if ratings[p] > ratings[p + 1]:
                res[p] += 1
        else:
            continue
        print(f"{i=} {res=}")
    print(f"{res=}")
    return sum(res)



@profile_time_memory
def othersolution(ratings: List[int]) -> int :
    arr = [1] * len(ratings)
    
    for i in range(1, len(ratings)):
        if ratings[i - 1] < ratings[i]:
            arr[i] = arr[i - 1] + 1
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1] :
            arr[i] = max(arr[i], arr[i + 1] + 1)

    return sum(arr)


if __name__ == "__main__":
    # ratings = [1,0,2]
    # ratings = [1,2,2]
    ratings = [1,3,2,2,1]
    print(mysolution(ratings))
    print(othersolution(ratings))
