import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory
from typing import List


@profile_time_memory
def mysolution(gas: List[int], cost: List[int]) -> int:
    stations_cnt = len(gas)
    for i in range(stations_cnt):
        cur_station_idx = i
        cur_tank_gas = gas[cur_station_idx]
        for j in range(stations_cnt-1):
            print(f"{i=} {cur_station_idx=} {cur_tank_gas=}")
            if cur_tank_gas - cost[cur_station_idx] < 0:
                break
            cur_tank_gas -= cost[cur_station_idx]
            if cur_station_idx > stations_cnt:
                cur_station_idx = stations_cnt - cur_station_idx + 1
            else:
                cur_station_idx += 1
        if cur_tank_gas >= 0 and cur_station_idx == stations_cnt - 1:
            return i
    return -1


@profile_time_memory
def othersolution(gas: List[int], cost: List[int]) -> int:
    n = len(gas)

    start_index = n - 1
    end_index = n - 1

    stations_visited = 0
    gas_balance = 0

    while stations_visited < n:
        gas_balance += gas[end_index] - cost[end_index]
        stations_visited += 1

        end_index = (end_index + 1) % n

        while gas_balance < 0 and stations_visited < n:
            start_index -= 1

            gas_balance += gas[start_index] - cost[start_index]
            stations_visited += 1

    return -1 if gas_balance < 0 else start_index


if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    # print(mysolution(gas, cost))
    print(othersolution(gas, cost))
