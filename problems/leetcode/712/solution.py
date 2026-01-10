import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory

@profile_time_memory
def mysolution(s1: str, s2: str) -> int:
    # print(ord(s1[0]))
    # s1_ls = list(s1)
    # s2_ls = list(s2)

    # # 교집합인 문자열을 모두 추출
    # new_ls = []
    # for s1_e in s1_ls :
    #     if s1_e in s2_ls:
    #         new_ls.append(s1_e)
    pass



@profile_time_memory
def othersolution(s1: str, s2: str) -> int:
    dp = [[0 for x in range(len(s1)+1)] for y in range(len(s2)+1)]
    print(dp)
    for i in range(1, len(s1) +1):
        dp[0][i] = dp[0][i-1] + ord(s1[i-1])
    print(dp)
    for i in range(1, len(s2) + 1):
        dp[i][0] = dp[i-1][0] + ord(s2[i-1])
    print(dp)
    for i in range(1, len(s2)+1):
        for j in range(1, len(s1)+1):
            if s2[i-1] == s1[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + ord(s2[i-1]), dp[i][j-1] + ord(s1[j-1]))
            print(dp)
    return dp[len(s2)][len(s1)]
        

if __name__ == "__main__":
    s1 = "sea"
    s2 = "eat"
    mysolution(s1, s2)
    print(othersolution(s1, s2))
    