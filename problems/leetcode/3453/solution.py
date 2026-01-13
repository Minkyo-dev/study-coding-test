import sys
import os
from typing import List
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(squares: List[List[int]]) -> float:
    bsx1, bsy1, l1 = squares[0]
    bsx2, bsy2, l2 = squares[1]

    # y축 한번의 길이 구하는 함수
    def get_y_length(ty, bsy, sl) -> (int, int):
        if ty >= (bsy + sl) or ty <= bsy :
            return sl, sl
        elif bsy < ty and bsy+sl > ty:
            return bsy+sl - ty, ty-bsy
        else:
            print("ty, bsy, sl", ty, bsy, sl)
            return 
            
    
    above_s_size = 0
    below_s_size = 1
    max_ty = max(bsy1+l1, bsy2+l2)
    min_ty = min(bsy1, bsy2)

    ty = (max_ty) / 2

    while True:
        print(ty)
        # 각 사각형 위 아래 y축 길이 구하기
        ly_a_1, ly_b_1 = get_y_length(ty, bsy1, l1)
        ly_a_2, ly_b_2 = get_y_length(ty, bsy2, l2)

        # 위쪽 너비 
        above_s_size = ly_a_1 * l1 + ly_a_2 * l2

        # 아래 너비
        below_s_size = ly_b_1 * l1 + ly_b_2 * l2

        if abs(above_s_size - below_s_size) < 0.00001:
            break

        if above_s_size > below_s_size:
            min_ty = ty
            ty = (max_ty - min_ty) / 2
        elif above_s_size <= below_s_size:
            max_ty = ty
            ty = (max_ty - min_ty) / 2

        print(f"{above_s_size=}, {below_s_size=}, = {above_s_size - below_s_size} | {ty=}")
    print(ty)
    return ty



@profile_time_memory
def othersolution(squares: List[List[int]]) -> float:
    total = sum(l*l for _, _, l in squares)
    low = min(y for _, y, _ in squares)
    high = max(y + l for _, y, l in squares)
    def diff(Y: float) -> float:
        above = below = 0.0
        for _, y, l in squares:
            top = y + l
            if Y <= y:
                above += l*l
            elif Y >= top:
                below += l*l
            else:
                above += (top - Y) * l
                below += (Y - y) * l
        return above - below

    for _ in range(60):
        mid = (low + high) / 2
        if diff(mid) > 0:
            low = mid
        else:
            high = mid

    print(low)
    return round(low, 5)


if __name__ == "__main__":
    squares = [[0,0,2],[1,1,1]]
    mysolution(squares)
    othersolution(squares)
    