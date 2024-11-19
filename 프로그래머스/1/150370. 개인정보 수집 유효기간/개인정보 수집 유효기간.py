def solution(today, terms, privacies):
    answer = []
    
    # 일수로 계산
    # 연 : 12*28 = 336 , 월 : 28, 일 : 1
    today_arr = list(map(int, today.split('.')))
    today_num = today_arr[0]*336 + today_arr[1]*28 + today_arr[2]
    
    # 약관 종류별 보관 가능 기준일자 일수로 변환하여 저장
    terms_dict = dict()
    for term in terms:
        k, m = term.split()
        terms_dict[k] = today_num - int(m)*28
    
    for i, privacy in enumerate(privacies):
        date, kind = privacy.split()
        arr = list(map(int, date.split('.')))
        num = arr[0]*336 + arr[1]*28 + arr[2]
        
        if num <= terms_dict[kind]:
            answer.append(i+1)
    
    return answer