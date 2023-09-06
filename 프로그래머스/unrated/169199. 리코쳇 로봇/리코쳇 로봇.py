# bfs
from collections import deque

def solution(board):
    answer = 0
    
    # 보드게임판 크기
    N, M = len(board), len(board[0])
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    
    # 방문배열 저장
    v = [[False]*M for _ in range(N)]
    
    # 시작지점
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                v[i][j] = True
                # (말의 위치, 이동횟수, 방문배열)
                q.append((i, j, 0, v))
                break
        if len(q)>0:
            break
    
    arrive = False
    while q:
        x, y, cnt, visited = q.popleft()
        
        # 상하좌우 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 경계를 벗어나는 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            # 장애물이나 맨 끝에 부딪힐 때까지 이동
            while True:
                # 장애물
                if board[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                # 상하 이동일 때 경계
                if i<2 and (nx == 0 or nx == N-1):
                    break
                # 좌우 이동일 때 경계
                if i>=2 and (ny == 0 or ny == M-1):
                    break

                nx += dx[i]
                ny += dy[i]
                
            # 방문했던 지점인 경우
            if visited[nx][ny]:
                continue
                
            # 목표지점 'G'에 도달한 경우
            if board[nx][ny] == 'G':
                arrive = True
            
            visited[nx][ny] = True
            q.append((nx, ny, cnt+1, visited))
        
        if arrive:
            answer = cnt + 1
            break
    
    # 목표위치에 도달할 수 없는 경우 -1
    if answer == 0:
        answer = -1
    
    return answer