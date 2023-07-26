# bfs 활용 + set 자료구조

import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 말이 최대한 몇 칸을 지날 수 있는지 구하기
max_cnt = 0

q = set()
q.add((0, 0, board[0][0]))

while q:
    x, y, path = q.pop()

    max_cnt = max(len(path), max_cnt)

    # 상하좌우 인접한 칸으로 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 경계 확인
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue

        if board[nx][ny] in path:
            continue

        q.add((nx, ny, path + board[nx][ny]))

print(max_cnt)