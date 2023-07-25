# bfs 사용
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 단지에 속하는 집의 수 저장
complex = []


def bfs(r, c):
    q = deque()
    q.append((r, c))
    board[r][c] = -1

    cnt = 1
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if board[nx][ny] != '1':
                continue

            # 방문 처리
            board[nx][ny] = -1
            cnt += 1
            q.append((nx, ny))

    complex.append(cnt)


for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            bfs(i, j)

# 오름차순 정렬
complex.sort()
print(len(complex))
for x in complex:
    print(x)