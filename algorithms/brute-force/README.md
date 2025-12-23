# 완전탐색 (Brute Force)

## 핵심 개념
- 무식한 힘으로 모든 값을 대입해보는 방식
- **조합** : 주머니에서 공 2개를 한번에 꺼내는 시나리오 (순서 X)
- **순열** : 주머니에서 공 2개를 순서대로 꺼내는 시나리오 (순서 O)
- **부분집합** : 주머니에서 공 n개를 한번에 꺼내는 시나리오
- **완전탐색(Brute Force)** 은 가능한 경우의 수(해 공간, Search Space)를 **전부(또는 거의 전부) 시도**하여 정답을 찾는 방법이다.
- 구현이 단순하고 직관적이며, **정답 보장**이 강점이다. 대신 경우의 수가 커지면 시간 초과가 발생하기 쉽다.
- 코딩테스트에서 완전탐색은 보통 아래 형태로 나타난다.
  - **모든 조합/순열/부분집합**을 생성해서 검사
  - **모든 구간(연속 부분 배열)**을 검사
  - **모든 위치/상태**를 시뮬레이션(격자 이동, 규칙 기반 시뮬레이션)
  - **백트래킹(가지치기 포함 완전탐색)** 으로 불필요한 분기 제거
- 핵심 포인트는 “전부 해본다”가 아니라, **전부 해볼 수 있을 만큼 줄여서**(입력 크기, 가지치기, 사전계산) 풀 수 있는지 판단하는 것이다.

## 풀이 전략

1. **해 공간(가능한 경우) 정의**
   - 무엇을 “선택”하거나 “배치”하거나 “결정”해야 하는지 명확히 한다.
   - 예: n개 중 k개 선택(조합), n개 순서 배치(순열), 각 원소 포함/미포함(부분집합), 모든 구간(l,r) 등
2. **시간복잡도 상한 계산**
   - 최악 케이스에서 얼마나 시도하는지 먼저 계산한다.
   - 대표 상한 감각:
     - O(N^2): N ≈ 2만 이하면 경우에 따라 가능(언어/상수에 따라 다름), N≈1만은 안전한 편
     - O(N^3): N ≈ 400~800 수준에서 보통 한계
     - O(2^N): N ≈ 20 전후가 보통 한계
     - O(N!): N ≈ 10 전후가 보통 한계
3. **검증 함수(체크 함수) 분리**
   - 각 후보 해를 만들고, “정답 조건”을 판정하는 로직을 함수로 분리하면 실수와 복잡도가 줄어든다.
4. **가지치기(Pruning) 설계**
   - “더 진행해도 답이 좋아질 수 없는 경우”를 빠르게 중단한다.
   - 예: 현재 합이 이미 목표를 초과, 남은 최대치를 더해도 목표 미달, 중복 상태 방문 등
5. **중복 제거**
   - 동일한 상태를 여러 번 계산하지 않도록 메모이제이션/방문 체크를 고려한다(필요시).
   - 특히 순열/조합 생성에서 같은 값이 반복되는 입력은 중복 결과가 생길 수 있으므로 처리 필요.
6. **사전계산/누적합/정렬 등을 섞어 ‘완전탐색 가능한 형태’로 만든다**
   - 예: 구간 합을 O(1)로 만들기 위해 누적합 사용 → O(N^2) 완전탐색이 가능해짐

## 구현 패턴
```python
# 1. 조합 구하기
def get_combinations():
    from itertools import combinations

    pocket = [1, 2, 3, 4]
    return list(combinations(pocket, 2))

# 2. 순열 구하기
def get_permutations():
    from itertools import permutations

    pocket = [1, 2, 3, 4]
    return list(permutations(pocket, 2))

# 3. 부분집합 구하기
def get_bubunjibhap():
    from itertools import combinations

    pocket = [1, 2, 3, 4]
    subset = []
    for i in range(len(pocket) + 1):
        subset.extend(list(combinations(pocket, i)))
    return subset

# 0) 완전탐색의 기본 골격: 후보 생성 + 검증 + 최적 갱신
def brute_force_template(candidates):
    best = None  # 최대/최소/카운트 등 문제 목적에 맞게
    for cand in candidates:
        if is_valid(cand):
            best = update_best(best, cand)
    return best


def is_valid(cand):
    return True


def update_best(best, cand):
    return cand


# 1) 이중 루프: 모든 쌍/모든 구간 탐색
# - 예: 모든 (i, j) 조합 검사, 모든 연속 구간 [i..j] 검사 등
def all_pairs(arr):
    n = len(arr)
    best = None
    for i in range(n):
        for j in range(i + 1, n):
            # cand = (i, j) 또는 arr[i], arr[j]
            # 조건 검사 후 best 갱신
            pass
    return best


# 2) 모든 연속 구간 탐색 + 누적합으로 구간합 O(1) 만들기
def prefix_sums(arr):
    ps = [0]
    for x in arr:
        ps.append(ps[-1] + x)
    return ps

def range_sum(ps, l, r):
    # [l, r] 구간합
    return ps[r + 1] - ps[l]

def all_subarrays_sum(arr):
    n = len(arr)
    ps = prefix_sums(arr)
    best = None
    for l in range(n):
        for r in range(l, n):
            s = range_sum(ps, l, r)
            # s로 조건 검사/최적 갱신
            pass
    return best


# 3) 부분집합(2^N) 완전탐색: 비트마스크
def subset_by_bitmask(arr):
    n = len(arr)
    best = None
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])
        # subset 검사/갱신
        pass
    return best


# 4) 백트래킹(가지치기 포함 완전탐색): 조합/순열/부분집합 등에 활용
def backtracking(arr):
    n = len(arr)
    used = [False] * n
    best = None

    def dfs(path):
        nonlocal best

        # (A) 정답 후보 처리(필요한 시점에)
        # if is_valid(path):
        #     best = update_best(best, path)

        # (B) 종료 조건
        # if len(path) == k:
        #     return

        for i in range(n):
            if used[i]:
                continue

            # (C) 선택
            used[i] = True
            path.append(arr[i])

            # (D) 가지치기 예시: 조건상 더 진행 의미 없으면 중단
            # if not can_continue(path):
            #     path.pop()
            #     used[i] = False
            #     continue

            dfs(path)

            # (E) 되돌리기
            path.pop()
            used[i] = False

    dfs([])
    return best


# 5) 중복 원소가 있는 순열/조합에서 중복 결과 제거 패턴 (정렬 + 스킵)
def unique_permutations(nums):
    nums.sort()
    n = len(nums)
    used = [False] * n
    result = []

    def dfs(path):
        if len(path) == n:
            result.append(path[:])
            return

        prev = None
        for i in range(n):
            if used[i]:
                continue
            if prev is not None and nums[i] == prev:
                continue  # 같은 depth에서 동일 값은 스킵(중복 방지)

            prev = nums[i]
            used[i] = True
            path.append(nums[i])
            dfs(path)
            path.pop()
            used[i] = False

    dfs([])
    return result
```

## 주의사항
- **시간복잡도부터 반드시 계산**
  - 완전탐색은 구현 전에 최악의 경우 시도 횟수를 먼저 계산해야 한다.
  - 루프를 하나 추가할 때마다 복잡도가 어떻게 변하는지 항상 의식한다.

- **검증 비용도 전체 복잡도에 포함**
  - 후보를 많이 만들고 검증이 느리면 전체 시간은 급격히 증가한다.
  - 가능하면 검증 로직을 O(1) 또는 O(log N)으로 줄인다.
  - 누적합, 해시맵, 정렬 결과 재활용 등을 적극 활용한다.

- **백트래킹에서는 가지치기가 핵심**
  - 더 진행해도 답이 나아질 수 없는 경우는 즉시 탐색을 중단해야 한다.
  - 현재 상태의 최선(best-case) / 최악(worst-case) 경계를 기준으로 판단한다.

- **중복 상태와 중복 결과 주의**
  - 동일한 상태를 여러 번 탐색하지 않도록 방문 체크나 정렬 후 스킵 로직을 적용한다.
  - 특히 중복 원소가 있는 순열·조합 문제에서 중복 제거를 빼먹기 쉽다.

- **전역 변수 및 참조 공유 실수 주의**
  - 리스트를 결과에 저장할 때는 반드시 복사본을 저장한다.
  - Python에서 `nonlocal`, `global` 사용 시 갱신 위치를 명확히 한다.

- **정답 갱신 타이밍 명확화**
  - 완성된 해에서만 갱신해야 하는지,
  - 부분 상태에서도 갱신 가능한지 문제 요구사항을 정확히 구분한다.

- **완전탐색이 불가능해 보일 때의 전환 기준**
  - 입력 크기가 크면 투 포인터, 이분 탐색, DP, 그리디로 전환을 고려한다.
  - “모든 경우를 다 봐야 하는가?”를 항상 다시 질문한다.

## 문제 리스트
- [ ] [baekjoon 2309](../../problems/baekjoon/2309/) - the seven dwarfs
- [ ] [baekjoon 10819](../../problems/baekjoon/10819/) - maximize the difference
