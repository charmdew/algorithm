# bfs 2번
# 출발 지점에서 레버까지 최단거리
# 레버에서 도착 지점까지 최단거리

from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(s, e, R, C, maps):
    q = deque()
    
    # 최단 거리 저장 테이블
    dist = [[0]*C for _ in range(R)] 
    
    # 방문여부 저장
    visited = [[False]*C for _ in range(R)]
    
    # 시작점
    visited[s[0]][s[1]] = True
    q.append((s[0], s[1]))
    
    finish = False
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 경계 확인, 방문 체크
            if nx < 0 or nx >= R or ny < 0 or ny >= C or visited[nx][ny]:
                continue
            
            # 벽인 경우
            if maps[nx][ny] == 'X':
                continue
                
            dist[nx][ny] = dist[x][y] + 1
            visited[nx][ny] = True
            q.append((nx, ny))
                
            if [nx, ny] == e:
                finish = True
        if finish:
            break
    return dist[e[0]][e[1]]
            

def solution(maps):
    R = len(maps)
    C = len(maps[0])
    
    start, end, lever = [], [], []
    for i in range(R):
        for j in range(C):
            if maps[i][j] == 'S':
                start = [i, j]
            elif maps[i][j] == 'E':
                end = [i, j]
            elif maps[i][j] == 'L':
                lever = [i, j]
    
    # 시작 지점에서 레버까지 이동
    move_to_lever = bfs(start, lever, R, C, maps)
    
    # 레버에서 도착지점까지 이동
    move_to_end = bfs(lever, end, R, C, maps)
    
    # 둘 중 하나라도 목적지에 도착하지 못하는 경우는 -1
    if not move_to_lever or not move_to_end:
        answer = -1
    else:
        answer = move_to_lever + move_to_end
    
    return answer