import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution():
    pass

@profile_time_memory
def othersolution():
    pass

if __name__ == "__main__":
    mysolution()
    othersolution()
    