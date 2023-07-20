import sys
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().split())

fgraph = [[] for _ in range(N+1)]
# 역방향 저장
rgraph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, input().split())

    fgraph[a].append((b, w))
    rgraph[b].append((a, w))


def dijkstra(start, graph):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        t, now = heapq.heappop(q)

        if time[now] < t:
            continue
        for x, tt in graph[now]:
            cost = time[now] + tt

            if cost < time[x]:
                time[x] = cost
                heapq.heappush(q, (cost, x))


# 다익스트라 수행 (각 마을 ~ X 마을까지의 최단 소요시간)
time = [1e9]*(N+1)
time[X] = 0
dijkstra(X, rgraph)
result = [0] + [time[i] for i in range(1, N+1)]

# 다익스트라 수행 (X 마을 ~ 각 마을까지의 최단 소요시간)
time = [1e9]*(N+1)
time[X] = 0
dijkstra(X, fgraph)
for i in range(1, N+1):
    result[i] += time[i]

print(max(result))