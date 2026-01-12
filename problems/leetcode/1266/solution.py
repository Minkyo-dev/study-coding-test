import sys
import os
from typing import List
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(points: List[List[int]]) -> int:
    def get_move_count(start_p, next_p):
        x_dist = abs(next_p[0] - start_p[0])
        y_dist = abs(next_p[1] - start_p[1])
        move = 0
        while True:
            print("x_dist, y_dist", x_dist, y_dist)
            if x_dist == 0 and y_dist == 0 :
                break
            elif (x_dist >= 1) and (y_dist >= 1) :
                move += 1
                x_dist -= 1
                y_dist -= 1
            elif (x_dist > 0) :
                move += 1
                x_dist -= 1
            elif (y_dist > 0) :
                move += 1
                y_dist -= 1
        return move
    
    total_move = 0

    if len(points) == 1:
        return total_move
    for i in range(len(points) - 1):
        total_move += get_move_count(points[i], points[i+1])
    print(total_move)
    return total_move



    

@profile_time_memory
def othersolution(points: List[List[int]]) -> int:
    """
    reference : https://letzgorats.tistory.com/entry/%EB%A6%AC%ED%8A%B8%EC%BD%94%EB%93%9Cleetcodepython-1266-Minimum-Time-Visiting-All-Points
    """
    answer = 0

    for i in range(len(points) - 1):
        x1, y1 = points[i][0], points[i][1]
        x2, y2 = points[i+1][0], points[i+1][1]

        answer += max(abs(x1-x2), abs(y1-y2))  # Chevyshev distance
    return answer

if __name__ == "__main__":
    points = [[1,1],[3,4],[-1,0]]
    mysolution(points)
    print(othersolution(points))
    