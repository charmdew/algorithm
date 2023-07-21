import sys 
from collections import deque

input = sys.stdin.readline 

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 목초지 한변 길이 N, 소 마리수 K, 도로의 개수 R 입력
N, K, R = map(int, input().split())

# 도로 정보 
road = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    road[r1-1][c1-1].append((r2-1, c2-1))
    road[r2-1][c2-1].append((r1-1, c1-1))

# 소 위치 정보
cow = []
for _ in range(K):
    r, c = map(int, input().split())
    cow.append((r-1, c-1))

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 경계 확인
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            
            # 방문했던 곳인 경우 넘어감
            if visited[nx][ny]:
                continue
                
            # 길을 지나가야 하는 경우 넘어감
            if (nx, ny) in road[x][y]:
                continue
                
            visited[nx][ny] = True
            q.append((nx, ny))

# 길을 건너지 않으면 만날 수 없는 소가 몇 쌍인지 저장
pair = 0
for k in range(K):
    sx, sy = cow[k]

    visited = [[False]*N for _ in range(N)]
    visited[sx][sy] = True

    bfs(cow[k])

    # 나머지 소들을 방문했는지 확인
    for cx, cy in cow[k+1:]:
        if not visited[cx][cy]:
            pair += 1

print(pair)