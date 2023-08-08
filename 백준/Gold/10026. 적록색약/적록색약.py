# 그래프탐색
# 적록색약인 사람은 'R', 'G'를 'X'로  변환해서 구역 개수 구하기

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

pic = [list(input().strip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):  # 같은 구역 표시
    global N

    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 경계 확인, 방문 체크
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                continue

            # 같은 구역인 경우
            if pic[nx][ny] == pic[x][y]:
                visited[nx][ny] = True
                q.append((nx, ny))


# 구역 개수 저장
cnt = [0, 0]

# 적록색약이 아닌 사람이 봤을 때 구역 개수
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt[0] += 1


# 적록색약인 사람이 봤을 때 구역 개수
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if pic[i][j] in ('R', 'G'):
            pic[i][j] = 'X'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt[1] += 1

print(*cnt)