def mysolution(N: int, M: int, lesson: list[int]) -> int:
    """
    args:
      N : 강의의 수
      M : 블루레이 개수
      lesson : 강의 시간 목록

    return
      answer : 블루레이 크기(녹화 가능한 길이) 중 최소. 단위: 분
    """

    pass

def othersolution1(N: int, M: int, lesson: list[int]) -> int:
    # binary-search
    left = max(lesson)
    right = sum(lesson)
    answer = -1

    while left <= right :
        middle = (left + right) // 2  # 임시 블루레이 용량

        blueray_num = 1
        remain = middle
        for i in range(N):
            if remain < lesson[i]:
                blueray_num += 1
                remain = middle

            remain -= lesson[i]

        if blueray_num <= M :
            answer = middle
            right = middle - 1  # [left, middle - 1]
        else:
            left = middle + 1  # [middle + 1, right]

    return answer

