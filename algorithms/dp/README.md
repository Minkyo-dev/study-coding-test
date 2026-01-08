# 동적 계획법 (Dynamic Programming)

## 핵심 개념

- **메모이제이션**: Top-down (재귀 + 캐싱)
- **타뷸레이션**: Bottom-up (반복문)
- **점화식 수립**: 문제를 작은 부분 문제로 분해

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