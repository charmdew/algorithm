def solution(sizes):
    answer = 0
    
    N = len(sizes)
    
    # 가로 < 세로로 정렬
    for i in range(N):
        sizes[i].sort()
        
    sizes = list(zip(*sizes))

    answer = max(sizes[0])*max(sizes[1])
    
    return answer