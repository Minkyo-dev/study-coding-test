"""
빠른 입력 템플릿
"""
import sys
input = sys.stdin.readline

# 정수 하나
n = int(input())

# 정수 여러 개
a, b, c = map(int, input().split())

# 리스트
arr = list(map(int, input().split()))

# 2차원 리스트
graph = [list(map(int, input().split())) for _ in range(n)]

# 문자열 (개행 제거)
s = input().strip()

# 여러 줄 입력
data = [input().strip() for _ in range(n)]

