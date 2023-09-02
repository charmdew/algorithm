from collections import deque    

def solution(x, y, n):
    answer = 0
    
    INF = 1e9
    
    cnt = [INF] * (y+1)
    cnt[x] = 0
    
    q = deque()
    q.append((x, 0))
    
    while q:
        k, c = q.popleft()
        
        if k == y:
            answer = c
            break
        
        if k > y:
            continue
        
        if k+n <= y and cnt[k+n] == INF:
            cnt[k+n] = c+1
            q.append((k+n, c+1))
        if k*2 <= y and cnt[k*2] == INF:
            cnt[k*2] = c+1
            q.append((k*2, c+1))        
        if k*3 <= y and cnt[k*3] == INF:
            cnt[k*3] = c+1
            q.append((k*3, c+1))
    
    if x != y and answer == 0:
        answer = -1
    
    return answer