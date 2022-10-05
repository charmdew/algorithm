from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

time = 0    # 모두 녹아서 없어지는 데 걸리는 시간
cnt = 0     # 남아있는 치즈 수
result = 0  # 모두 녹기 한시간 전에 남아있는 치즈 조각 수

# 치즈 개수 세기
for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            cnt += 1


def boundary():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                bfs(i, j)
                return


def bfs(a, b):
    global cnt, result

    visited = [[False]*M for _ in range(N)]

    q = deque()
    q.append((a, b))
    visited[a][b] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cheese = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M or visited[nx][ny]:
                continue

            # 치즈가 있는 곳이라면
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                cheese.append((nx, ny))
            if board[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = True

    for cx, cy in cheese:
        board[cx][cy] = 0

    cnt -= len(cheese)      # 남은 치즈 개수 줄이기
    result = len(cheese)    # 현재 시간에 녹은 치즈 수


while cnt > 0:
    time += 1
    boundary()

print(time)
print(result)