# 자주 쓰는 트릭

## Python 문법

### 입력
```python
import sys
input = sys.stdin.readline

# 개행 제거 주의
s = input().strip()
```

### 무한대
```python
INF = int(1e9)  # 10억
INF = float('inf')  # 실수 무한대
```

### 2차원 리스트 초기화
```python
# 올바른 방법
arr = [[0] * m for _ in range(n)]

# 잘못된 방법 (얕은 복사)
arr = [[0] * m] * n  # ❌
```

### 리스트 정렬
```python
# 튜플 정렬 (첫 번째 → 두 번째 순)
arr.sort()  # 오름차순
arr.sort(reverse=True)  # 내림차순

# 커스텀 정렬
arr.sort(key=lambda x: (x[0], -x[1]))  # 첫째 오름, 둘째 내림
```

### Counter
```python
from collections import Counter

arr = [1, 1, 2, 3, 3, 3]
counter = Counter(arr)
# Counter({3: 3, 1: 2, 2: 1})

# 가장 많은 N개
counter.most_common(2)  # [(3, 3), (1, 2)]
```

## 알고리즘 트릭

### 누적 합
```python
# 구간 합 O(1)
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i-1] + arr[i-1]

# arr[l:r+1]의 합
sum_value = prefix[r+1] - prefix[l]
```

### 투 포인터
```python
left, right = 0, 0
result = 0

while right < n:
    # right 확장
    current += arr[right]

    # 조건 위반시 left 이동
    while current > target:
        current -= arr[left]
        left += 1

    result += (right - left + 1)
    right += 1
```

### 슬라이딩 윈도우
```python
# 크기 k 윈도우
window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, n):
    window_sum += arr[i] - arr[i-k]
    max_sum = max(max_sum, window_sum)
```

### 비트마스킹
```python
# i번째 비트 확인
if mask & (1 << i):
    pass

# i번째 비트 켜기
mask |= (1 << i)

# i번째 비트 끄기
mask &= ~(1 << i)

# 켜진 비트 개수
bin(mask).count('1')
```

### 좌표 압축
```python
# 좌표 범위가 크지만 개수가 적을 때
unique = sorted(set(arr))
compressed = {v: i for i, v in enumerate(unique)}
arr = [compressed[x] for x in arr]
```

## 자주 하는 실수

### 인덱스
- Python은 0-based
- 문제는 1-based인 경우 많음
- 범위 조심: `range(n)`은 0~n-1

### 깊은 복사
```python
import copy

# 1차원
new_arr = arr[:]
new_arr = arr.copy()

# 2차원
new_arr = copy.deepcopy(arr)
```

### 재귀 깊이
```python
import sys
sys.setrecursionlimit(10**6)
```

### 나누기
```python
# 정수 나누기
a // b  # 몫
a % b   # 나머지

# 올림
import math
math.ceil(a / b)
-(-a // b)  # 트릭
```

