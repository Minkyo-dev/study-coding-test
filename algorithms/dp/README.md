# 동적 계획법 (Dynamic Programming)

## 핵심 개념

- **메모이제이션**: Top-down (재귀 + 캐싱) : 이미 계산된 결과를 저장해 두었다가 필요할 때 재사용 하는 기법. 이를 통해 동일한 게산을 반복하지 않아도 되기에 프로그램의 실행 시간을 대폭 줄일 수 있다.
- **타뷸레이션**: Bottom-up (반복문)
- **점화식 수립**: 문제를 작은 부분 문제로 분해 : 하위 문제들 사이에서 관계를 수학적으로 표현한 식. 이 식을 통해서 다음 단계의 문제 해결에 필요한 값을 이전 단계의 결과로부터 도출할 수 있다.

### DP 유형

1. **1차원 DP**: 피보나치, 계단 오르기
2. **2차원 DP**: LCS, 배낭 문제, 편집 거리
3. **비트마스킹 DP**: 외판원 순회 (TSP)
4. **트리 DP**: 트리에서의 최적화

## 풀이 전략

1. 상태 정의: `dp[i]`가 무엇을 의미하는지 명확히
2. 점화식 도출: 이전 상태로부터 현재 상태 계산
3. 초기값 설정: Base case 확인
4. 계산 순서: 의존성 고려

## 구현 패턴
```python

```

## 주의사항

## 문제 리스트



- [ ] [leetcode 1458](../../problems/leetcode/1458/) - Max Dot Product of Two Subsequences
- [ ] [leetcode 712](../../problems/leetcode/712/) - Minimum ASCII Delete Sum for Two Strings
- [ ] [baekjoon 85](../../problems/baekjoon/85/) - Maximal Rectangle