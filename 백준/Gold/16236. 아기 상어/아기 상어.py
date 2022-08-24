import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

"""
공간 상태 입력
    0: 빈 칸
    1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
    9: 아기 상어의 위치
"""
space = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어 크기
size = 2

# 아기 상어 위치
sx, sy = -1, -1
for i in range(N):
    for j in range(N):
        if space[i][j] ==9:
            sx, sy = i, j

# 상, 좌, 우, 하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간
time = 0

# 아기 상어가 먹은 물고기 수
eatCnt = 0

# 이동하기 (bfs로 이동하면서 가장 먼저 찾은 먹을 수 있는 물고기)
def move(a, b):
    visited = [[False]*N for _ in range(N)]
    # print(a, b)
    global time, sx, sy

    q = deque()
    q.append((a, b))
    visited[a][b] = True

    fish = []

    t = 0
    find = False
    while q:
        qSize = len(q)
        t += 1

        for qs in range(qSize):
            x, y = q.popleft()

            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                # 경계 체크
                if nx<0 or N<=nx or ny<0 or N<=ny:
                    continue

                if visited[nx][ny]:
                    continue

                # 자신의 크기 >= 상태값 (이동 가능)
                if size >= space[nx][ny]:
                    visited[nx][ny] = True

                    if 0 < space[nx][ny] < size:
                        # print("먹을 수 있는 물고기", nx, ny, space[nx][ny])
                        # 0 < 상태값 < 자신의 크기: 먹을 수 있는 물고기
                        fish.append((nx, ny))
                        find = True
                        continue

                    q.append((nx, ny))

        if find:
            break

    # 먹을 수 있는 물고기가 있는 경우
    if len(fish) > 0:
        # 가장 위, 왼쪽에 있는 물고기 찾기
        fish.sort()

        # 이동
        sx, sy = fish[0]

        # 이동하는데 걸린 시간 추가
        time += t

        # 현재 위치에 있는 물고기 먹기
        eat(sx, sy)
        return True

    # 먹을 수 있는 물고기가 없는 경우 > 끝!!
    else:
        print(time)
        return False


# 먹기
def eat(x, y):
    global size, eatCnt
    # 먹은 물고기 수 증가
    eatCnt += 1

    # 물고기를 먹으면, 그 칸은 빈 칸이 된다.
    space[x][y] = 0

    # 자신의 크기와 같은 수의 물고기를 먹을 때마가 크기가 1 증가
    if eatCnt == size:
        size += 1
        eatCnt = 0  # 먹은 물고기 수 초기화


# 처음 시작 위치 빈칸으로 변경
space[sx][sy] = 0

while True:
    # 더 이상 먹을 수 있는 물고기가 없으면 종료!
    if not move(sx, sy):
        break