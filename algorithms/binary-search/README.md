# 이분 탐색 (Binary Search)

## 핵심 개념

- **정렬된 데이터** 필요
- **시간 복잡도**: O(log N)
- **파라메트릭 서치**: 결정 문제로 변환
- **탐색하려는 값** 과 **탐색범위[하한, 상한]**를 먼저 찾아내는 것이 중요.
- 정렬된 데이터 에서 탐색 범위를 절반씩 줄여가며 답을 찾는 알고리즘

- 탐색 대상은 값 그 자체일 수도 있고, 조건을 처음/마지막으로 만족하는 지점일 수도 있음

- 핵심은 “정답이 존재하는 구간이 단조(monotonic)하게 줄어든다”는 성질

- 시간복잡도: O(log N)

## 풀이 전략

1. 배열 또는 탐색 공간이 정렬되어 있는지 확인
2. 탐색 대상이 값인지, 조건을 만족하는 경계인지 정의
3. 탐색 구간을 [left, right] 또는 [left, right] 중 하나로 통일
4. mid 기준으로 탐색 범위를 줄이는 규칙 수립
5. 종료 조건과 반환 값(값 / 인덱스 / 가능 여부)을 명확히 정의

## 구현 패턴

```python
# 1. 기본 이분 탐색
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# 2. lower_bound (target 이상의 첫 위치)
def lower_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

# 3. upper_bound (target 초과의 첫 위치)
def upper_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left

# 4. 파라메트릭 서치 (결정 문제)
def parametric_search(arr, target):
    """
    조건을 만족하는 최댓값/최솟값 찾기
    """
    def check(mid):
        # 조건 체크 함수
        return True

    left, right = 0, max(arr)
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            result = mid
            left = mid + 1  # 더 큰 값 탐색
        else:
            right = mid - 1

    return result

# bisect 라이브러리 사용
import bisect

arr = [1, 2, 4, 4, 8]
target = 4

# lower_bound
idx = bisect.bisect_left(arr, target)

# upper_bound
idx = bisect.bisect_right(arr, target)

# 정렬 상태 유지하며 삽입
bisect.insort(arr, 5)
```

## 주의사항

- 값 탐색 이분 탐색은 반드시 정렬이 전제

- mid 계산 시 `left = mid, right = mid` 형태는 무한 루프 위험

- 구간 정의([left, right] vs [left, right])를 끝까지 유지

- 조건 이분 탐색은 can_do 함수가 단조성을 가져야 함

- 조건 만족 시 즉시 종료하지 말고 더 나은 해가 있는지 확인

## 문제 리스트
- [ ] [백준 2512](../../problems/baekjoon/2512/) - 예산
- [ ] [baekjoon 2343](../../problems/baekjoon/2343/) - guitar lesson
- [ ] [leetcode 3453](../../problems/leetcode/3453/) - Separate Squares 1