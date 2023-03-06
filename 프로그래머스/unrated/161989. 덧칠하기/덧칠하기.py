import math

def solution(n, m, section):
    answer = 1
    
    L = len(section)
    
    pre = section[0]
    for i in range(1, L):
        if pre + m > section[i]:
            continue
        
        # 페인트칠 +1
        answer += 1
        pre = section[i]
    
    return answer