def solution(n, l, r):
    answer = 0
    
    for x in range(l-1, r):        
        if x % 5 == 2:
            continue
            
        zero = False
        for i in range(n):
            x //= 5
            if x <= 0:
                break
            if x % 5 == 2:
                zero = True
                break
                
        if not zero:
            answer += 1
    
    return answer