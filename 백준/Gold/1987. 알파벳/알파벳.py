# dfs 활용

import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 알파벳 나왔는지 여부
visited = [False] * 26

# 말이 최대한 몇 칸을 지날 수 있는지 구하기
max_cnt = 0


def dfs(x, y, cnt):
    global R, C, max_cnt

    max_cnt = max(max_cnt, cnt)

    # 상하좌우 인접한 칸으로 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 경계 확인
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue

        idx = ord(board[nx][ny])-ord('A')
        # 알파벳 나왔는지 확인
        if visited[idx]:
            continue

        visited[idx] = True
        dfs(nx, ny, cnt+1)
        visited[idx] = False


# 좌측 상단에서 시작
visited[ord(board[0][0])-ord('A')] = True
dfs(0, 0, 1)
print(max_cnt)