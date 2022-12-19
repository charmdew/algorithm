def solution(survey, choices):
    answer = ''
    
    # 성격 유형
    kind = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    
    # 성격 지표
    mbti = [[kind[2*i], kind[2*i+1]] for i in range(len(kind)//2)]
    
    # 성격 유형 점수
    score = {k:0 for k in kind}
    
    for i in range(len(survey)):
        # '모르겠음' 선택한 경우 넘어감
        if choices[i]==4:
            continue
        
        # d: 동의 여부(0: 비동의, 1: 동의)
        # r: 정도 (1: 약간, 2: 중간, 3: 매우)
        d, r = divmod(choices[i], 4)
        if d==0: r = 4-r
        
        # 성격 유형 점수 더하기
        score[survey[i][d]] += r
            
    # 성격 유형 검사 결과
    for i in range(4):
        # 지표에서 성격 유형 판단
        x = mbti[i][0]

        if score[mbti[i][0]]<score[mbti[i][1]]:
            x = mbti[i][1]

        answer += x
    
    return answer