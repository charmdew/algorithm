def solution(brown, yellow):
    answer = []
    
    ## 시간 초과 코드
    # for i in range(yellow+1):
    #     for j in range(i, yellow+1):
    #         if i*j == yellow and i+j == (brown-4)//2:
    #             answer.append(j+2)
    #             answer.append(i+2)
    
    # 카펫의 노란색의 가로길이를 w, 세로길이를 h라 할때
    #   yellow = w*h
    #   brown = 2*w + 2*h + 4
    # w+h = (brown-4)//2
    # 2 <= w+h <= 2498, h <= w
    for h in range(1250):
        w = (brown-4)//2 - h
    
        if w*h == yellow:
            # 카펫의 가로 세로 길이는 노란색에서 +2씩
            answer = [w+2, h+2]
            break
            
    return answer