from collections import deque

N = int(input())

# 각 구역별 인구 수
population = [0] + list(map(int, input().split()))

answer = 1001  # 두 선거구의 인구 차이의 최솟값 저장

graph = [[] for i in range(N+1)]
for i in range(1, N+1):
    info = list(map(int, input().split()))
    graph[i] = info[1:]


# N개의 구역 중 1개, 2개, .. N//2개 뽑는 경우
def comb(start, r):
    if len(area1) == r:
        area2 = [x for x in range(1, N + 1) if x not in area1]
        check(area1, area2)
        return

    for i in range(start, N+1):
        area1.append(i)
        comb(i+1, r)
        area1.pop()


# 선거구 안의 구역들이 인접해 있는지 확인
# 인접해 있다면 인구수 차이 계산 후 최솟값 업데이트
def check(area1, area2):
    global answer

    a1 = bfs(area1)
    # 선거구 1에 있는 구역들이 인접하지 않은 경우
    if not a1:
        return

    a2 = bfs(area2)
    # 선거구 2에 있는 구역들이 인접하지 않은 경우
    if not a2:
        return

    answer = min(answer, abs(a1-a2))


def bfs(area):
    q = deque([area[0]])

    cnt = 1     # 연결된 구역 수 저장
    peopleCnt = 0  # 선거구의 인구수 저장

    visited = [False] * (N + 1)
    visited[area[0]] = True   # 처음 구역 방문처리

    while q:
        x = q.popleft()
        # print(x, population[x])
        peopleCnt += population[x]

        for to in graph[x]:
            # 방문하지 않았고, 해당 선거구에 속한다면
            if not visited[to] and to in area:
                cnt += 1
                q.append(to)
                # 방문처리
                visited[to] = True

    # print("bfs", cnt, len(area))
    if cnt == len(area):
        return peopleCnt
    else:
        return False


for i in range(1, N//2+1):
    area1, area2 = [], []
    comb(1, i)

print(-1 if answer == 1001 else answer)