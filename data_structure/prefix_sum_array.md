# 누적합 (Prefix Sum) 배열

## 개념
누적합(Prefix Sum) 배열이란, 주어진 수열에서 구간 합을 빠르게 계산하기 위해 각 인덱스까지의 합을 미리 계산해 저장한 배열입니다.

<img src="./img/스크린샷 2026-01-10 221253.png" width="500">

## 예시
```python
arr = [1, 2, 3, 4, 5]
prefix_sum = [0] * (len(arr) + 1)
for i in range(1, len(arr) + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
print(prefix_sum)
```

## 언제 쓰냐?
- 구간 합 질의가 많고, 배열 값이 변하지 않거나(정적) 거의 안 변할 때
- 평균/부분합/누적확률/슬라이딩 윈도우 합(고정 길이) 같은 것도 사실상 누적합으로 귀결

psum :
$$
psum[i] = sum(arr[0:i])
$$

$$
psum[i:j] = psum[j] - psum[i]
$$


