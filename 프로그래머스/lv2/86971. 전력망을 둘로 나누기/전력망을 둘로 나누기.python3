# 두 전력망이 가지고 있는 송전탑 개수의 차이 구하기
def count(graph, n):
    # 송전탑 방문 여부 저장
    visited = [False]*(n+1)
    
    # 두 전력망의 송전탑 개수 저장
    cnt = [1]*2
    
    x = 0
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            
            vs = [i]
            while vs:
                v = vs.pop()
                # 전력망이 갖게 되는 송전탑 개수 구하기
                for g in graph[v]:
                    # 방문하지 않은 송전탑인 경우
                    if not visited[g]:
                        visited[g] = True
                        cnt[x]+=1   
                        vs.append(g)
            x+=1
    return abs(cnt[0]-cnt[1])

def solution(n, wires):
    answer = -1
    
    # 두 전력망이 가지고 있는 송전탑 개수의 차이 저장
    diff = 100 
    
    # 완전 탐색
    for i in range(n-1):
        # 전선들 중 하나 끊기
        wire = wires[:i]+wires[i+1:]
        
        # 전선 정보 저장
        graph = [[] for _ in range(n+1)]
        for v1, v2 in wire:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        # 
        diff = min(diff, count(graph, n))
        
    answer = diff
        
    return answer