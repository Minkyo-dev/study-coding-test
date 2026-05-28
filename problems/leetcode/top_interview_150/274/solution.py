import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory
from typing import List


@profile_time_memory
def mysolution(citations: List[int]) -> int:
    n = len(citations) 
    if n == 1 and citations[0] == 0:
        return 0
    if n == 1:
        return 1
    
    desc_citations = sorted(citations, reverse=True)

    for idx, e in enumerate(desc_citations) :
        print(idx, e)
        if e >= (idx + 1) :
            continue
        else:
            return idx
    return n


@profile_time_memory
def othersolution():
    pass


if __name__ == "__main__":
    citations = [3,0,6,1,5]
    citations = [1,3,1]
    citations = [11,15]
    print(mysolution(citations))
    othersolution()
