import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory
from random import choice


@profile_time_memory
class RandomizedSet:
    """
    # Your RandomizedSet object will be instantiated and called as such:
    # obj = RandomizedSet()
    # param_1 = obj.insert(val)
    # param_2 = obj.remove(val)
    # param_3 = obj.getRandom()
    """
    def __init__(self):
        self.nums_map = {}
        self.nums_list = []
        

    def insert(self, val: int) -> bool:
        is_exist = val in self.nums_map
        if not is_exist:
            self.nums_map[val] = len(self.nums_list)
            self.nums_list.append(val)
        return not is_exist

    def remove(self, val: int) -> bool:
        is_exist = val in self.nums_map
        if is_exist:
            idx = self.nums_map[val]
            last_val = self.nums_list[-1]
            self.nums_list[idx] = last_val
            self.nums_list.pop()
            self.nums_map[last_val] = idx
            del self.nums_map[val]
        return is_exist

    def getRandom(self) -> int:
        return choice(self.nums_list)


@profile_time_memory
def othersolution():
    pass


if __name__ == "__main__":
    obj = RandomizedSet()
    othersolution()
