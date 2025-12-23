# 정렬 (Sort)

## 핵심 개념
- 배열의 원소를 순서에 맞게 재배치
- **정렬(Sort)** 은 데이터 집합을 **특정 기준(오름차순 / 내림차순 등)** 에 따라 순서대로 재배치하는 알고리즘이다.
- 많은 알고리즘 문제에서 정렬은 **전처리(preprocessing)** 역할을 하며, 이후 로직을 단순화하거나 시간복잡도를 낮추는 데 핵심적인 역할을 한다.
- 정렬 자체가 목적이 되는 문제도 있지만, 대부분은 아래와 같은 문제 해결을 위해 사용된다.
  - 이분 탐색, 투 포인터 적용 가능 상태 만들기
  - 중복 제거, 그룹화, 범위 처리 단순화
  - 그리디 알고리즘의 최적 선택 조건 만족
- 일반적인 비교 기반 정렬의 시간복잡도 하한은 **O(N log N)** 이다.

## 풀이 전략
1. **정렬이 필요한 이유부터 판단**
   - 단순히 문제에서 “정렬하라”고 해서가 아니라,
   - 정렬을 하면 이후 로직이 단순해지거나 더 빠르게 풀 수 있는지 먼저 판단한다.
2. **정렬 기준 명확화**
   - 오름차순 / 내림차순
   - 단일 기준인지, 다중 기준인지 (예: 1순위, 2순위)
3. **정렬 안정성(stable sort) 필요 여부 판단**
   - 같은 값의 상대적 순서가 중요한 문제인지 확인
4. **정렬 후 어떤 알고리즘과 결합할지 결정**
   - 투 포인터, 이분 탐색, 그리디, 스캔, 중복 제거 등
5. **정렬 비용을 포함한 전체 시간복잡도 계산**
   - 정렬 O(N log N) + 이후 로직 비용을 합산해 제한 시간 내 가능한지 확인

## 구현 패턴
```python
# 1) 기본 오름차순 / 내림차순 정렬
arr.sort()                 # 오름차순
arr.sort(reverse=True)     # 내림차순

# 또는
sorted_arr = sorted(arr)
sorted_desc = sorted(arr, reverse=True)


# 2) 커스텀 기준 정렬 (key 함수)
# - key 함수의 반환값을 기준으로 정렬됨
arr.sort(key=lambda x: x[1])            # 두 번째 값 기준
arr.sort(key=lambda x: (x[0], -x[1]))   # 다중 기준: x[0] 오름차순, x[1] 내림차순


# 3) 문자열 정렬
words.sort()                             # 사전순
words.sort(key=len)                     # 길이 기준
words.sort(key=lambda w: (len(w), w))   # 길이 → 사전순


# 4) 정렬 + 중복 제거 패턴
arr.sort()
unique = []
for x in arr:
    if not unique or unique[-1] != x:
        unique.append(x)


# 5) 정렬 + 투 포인터 / 스캔 패턴
arr.sort()
n = len(arr)
for i in range(n):
    # arr[i]를 기준으로 이후 로직 처리
    pass


# 6) 정렬 + 이분 탐색 패턴
import bisect

arr.sort()
idx = bisect.bisect_left(arr, target)   # lower bound
idx = bisect.bisect_right(arr, target)  # upper bound


# 7) 인덱스를 유지한 채 정렬 (원래 위치가 필요한 경우)
indexed = list(enumerate(arr))
indexed.sort(key=lambda x: x[1])
# indexed: (원래 인덱스, 값)


# 8) 정렬 대신 Counting Sort 개념 적용 (값의 범위가 작을 때)
from collections import Counter

cnt = Counter(arr)
sorted_arr = []
for k in sorted(cnt):
    sorted_arr.extend([k] * cnt[k])
```

## 주의사항
- 정렬이 항상 필요한 것은 아니다

    - 해시, 누적합, DP 등으로 정렬 없이 해결 가능한 문제도 많다.

- 정렬 기준 실수 주의

    - 다중 기준 정렬에서 key 순서가 바뀌면 결과가 완전히 달라진다.

- 정렬 후 인덱스 의미 상실

    - 원래 위치 정보가 필요하면 (값, 인덱스) 형태로 함께 정렬한다.

- 정렬 안정성(stable sort) 인식

    - Python의 sort, sorted 는 안정 정렬이므로 이를 활용할 수 있다.

- 실수(float) 정렬 주의

    - 부동소수점 오차로 인해 예상과 다른 결과가 나올 수 있다.

- 정렬 이후 알고리즘 전환 포인트 인식

    - 정렬 + 투 포인터 / 이분 탐색 / 그리디는 코딩 테스트의 핵심 패턴이다.


## 문제 리스트
- [ ] [baekjoon 1946](../../problems/baekjoon/1946/) - new employee
- [ ] [baekjoon 11728](../../problems/baekjoon/11728/) - concat array
