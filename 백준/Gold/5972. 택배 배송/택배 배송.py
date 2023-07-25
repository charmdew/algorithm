# 다익스트라
# 1~N까지 가는 최소비용 구하기

import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    cost[start] = 0

    while q:
        c, now = heapq.heappop(q)

        # 이미 처리된 적이 있는 곳이라면 무시
        if cost[now] < c:
            continue

        for x, cc in graph[now]:
            nc = c + cc

            if nc < cost[x]:
                cost[x] = nc
                heapq.heappush(q, (nc, x))


cost = [1e9] * (N+1)
dijkstra(1)
print(cost[N])