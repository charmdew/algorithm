from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

iceberg = [list(map(int, input().split())) for _ in range(N)]

# 빙산의 위치, 갯수 저장
pos, cnt = [], 0
for i in range(N):
    for j in range(M):
        if iceberg[i][j] > 0:
            cnt += 1
            pos.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 덩어리 확인
def bfs(start, N, M):
    visited = [[0]*M for _ in range(N)]
    visited[start[0]][start[1]] = 1
    count = 1

    q = deque([start])
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or N<=nx or ny<0 or M<=ny:
                continue
            if iceberg[nx][ny]>0 and visited[nx][ny]==0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                count +=1
    return count


def melt(pos, N, M):
    global cnt
    zero = [[0]*M for _ in range(N)]
    for x, y in pos:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or N<=nx or ny<0 or M<=ny:
                continue
            if iceberg[nx][ny]==0:
                zero[x][y]+=1

    remove_list = []
    for x, y in pos:
        # 각 칸에 저장된 높이는 0보다 더 줄어들지 않음
        iceberg[x][y] = max(iceberg[x][y]-zero[x][y], 0)
        # print(x, y, iceberg[x][y])
        if iceberg[x][y] == 0:
            cnt -= 1
            remove_list.append((x, y))
    for x, y, in remove_list:
        pos.remove((x, y))


answer = 0
# 덩어리가 1개인지 확인
while cnt == bfs(pos[0], N, M):
    # 빙산 녹이기
    melt(pos, N, M)
    answer += 1

    if len(pos) == 0:
        answer = 0
        break

print(answer)