import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(N: int, P: list[int]) -> int:
    minimum_time_sum = 0

    P = sorted(P)

    for i in range(N):
        # print(P[0:i+1])
        minimum_time_sum += sum(P[0:i+1])
    return minimum_time_sum

@profile_time_memory
def othersolution(N: int, P: list[int]):
    P = sorted(P)

    waiting = [0] * N
    waiting[0] = P[0]

    for i in range(1, N):
        waiting[i] = waiting[i - 1] + P[i]
    
    return sum(waiting)

if __name__ == "__main__":
    N = 5
    P = [3, 1, 4, 3, 2]
    print(mysolution(N, P))
    print(othersolution(N, P))
    