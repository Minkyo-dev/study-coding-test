# 투포인터 (Two Pointer)

## 핵심 개념
- **투 포인터(Two Pointers)** 는 배열이나 리스트에서 **두 개의 인덱스(포인터)** 를 사용해 탐색 범위를 조절하며 문제를 해결하는 알고리즘 기법이다.
- 보통 `left`, `right` 두 포인터를 사용하며, 조건에 따라 한쪽 또는 양쪽 포인터를 이동시킨다.
- 모든 경우를 탐색하지 않고도 답을 찾을 수 있어, **완전탐색(O(N^2))을 O(N)** 으로 줄이는 데 자주 사용된다.
- 투 포인터는 다음 전제가 있을 때 가장 효과적이다.
  - 배열이 **정렬되어 있거나**
  - 포인터 이동에 따라 **조건이 단조(monotonic)** 하게 변하는 경우

## 풀이 전략

1. **포인터의 의미를 먼저 정의**
   - `left`, `right`가 무엇을 의미하는지 명확히 한다.
   - 예: 구간의 시작/끝, 두 원소의 비교 위치 등
2. **포인터 이동 규칙 설계**
   - 조건을 만족할 때 어떤 포인터를 이동할지
   - 조건을 만족하지 않을 때 어떻게 범위를 조절할지 결정
3. **불변 조건(invariant) 유지**
   - 예: `left <= right`, 혹은 현재 구간이 항상 조건을 만족/불만족
4. **정렬 여부 확인**
   - 양끝에서 좁혀오는 방식은 보통 정렬이 전제
5. **종료 조건 명확화**
   - `right == n` 도달
   - `left >= right` 등 무한 루프 방지
6. **시간복잡도 확인**
   - 각 포인터는 최대 N번 이동 → 전체 O(N)

## 구현 패턴
- 아래는 가장 대표적인 슬라이딩 윈도우(연속 부분 구간) 템플릿입니다.

(예: “조건을 만족하는 최소 길이 구간” 또는 “조건 만족 여부로 확장/축소” 형태)
```python
def two_pointers(arr):
    n = len(arr)
    left = 0
    current = 0  # 윈도우 내 누적값(합/카운트/조건 관련 값)

    for right in range(n):
        # 1) right 확장
        current += arr[right]

        # 2) 조건을 만족하는 동안 left를 줄여(축소) 최적화
        while condition(current, left, right):
            # answer 갱신 로직 (예: 최소 길이, 최대 길이, 개수 등)
            # ans = min(ans, right - left + 1)
            current -= arr[left]
            left += 1

    return  # ans 또는 원하는 결과


def condition(current, left, right):
    # 문제 조건에 맞게 구현 (예: current >= S)
    return False

```

- 정렬 배열에서 양끝 포인터 패턴
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1

    return False

```


## 주의사항
- 정렬이 필요한 문제인지 확인

    - “양끝 포인터” 류는 보통 정렬이 전제(또는 입력이 이미 정렬)

- 슬라이딩 윈도우가 성립하는 조건 확인

    - 예: “부분합 ≥ S” 같은 경우 원소가 모두 양수면 윈도우 축소/확장이 단조롭게 동작

    - 음수가 섞이면 단순 투 포인터로 해결이 어려워지고 다른 기법(누적합+해시, 이분탐색 등)이 필요할 수 있음

- 경계 처리

    - left, right가 가리키는 구간이 [left, right]인지 [left, right)인지 혼동 금지

- 무한 루프 방지

    - while 내부에서 반드시 left 또는 right가 이동하도록 보장

- 답 갱신 타이밍

    - “조건 만족 시 갱신”인지 “조건 불만족 시 갱신”인지 문제에 따라 달라짐


## 문제 리스트
- [ ] [baekjoon 2003](../../problems/baekjoon/2003/) - sum of numbers 2
