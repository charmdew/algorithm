# df 사용
import sys

input = sys.stdin.readline

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 단지에 속하는 집의 수 저장
complex = []


def dfs(x, y):
    global cnt

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
        dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            board[i][j] = -1
            cnt = 1
            dfs(i, j)
            complex.append(cnt)

# 오름차순 정렬
complex.sort()
print(len(complex))
for x in complex:
    print(x)