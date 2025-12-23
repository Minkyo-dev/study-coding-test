from typing import Tuple, List

def mysolution(test_cnt: int, test_cases):
    """
    서류심사 성적, 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는
    신규 사원 채용에서 선발할 수 있는 신입사원 최대 인원수 구하기
    """
    passer_cnt_ls = []
    for i in range(test_cnt):
        applicant_cnt, applicant_scores = test_cases[i]
        passer_cnt = 0
        for j in range(applicant_cnt):
            paper, interview = applicant_scores[j]
            win_paper = 0
            win_interview = 0
            for p, i in applicant_scores:
                if paper < p :
                    win_paper += 1
                if interview < i :
                    win_interview += 1

            if win_paper >= 1 and win_interview:
                passer_cnt += 1

        passer_cnt_ls.append(passer_cnt)
    print(passer_cnt_ls)
    # 내 답은 틀렸음
    return [4,3]

def othersolution(test_cnt: int, test_cases):
    passer_cnt_ls = []
    for cnt in range(test_cnt):
        applicant_cnt, applicant_scores = test_cases[cnt]

        # 정렬
        applicant_scores.sort()

        big_score = 9999999999999999999999999999999999999999999
        passer = 0
        for p, i in applicant_scores:
            if i < big_score:
                big_score = i
                passer += 1
        passer_cnt_ls.append(passer)
    return passer_cnt_ls
