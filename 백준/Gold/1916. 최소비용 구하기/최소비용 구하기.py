"""
다익스트라 이용!
"""

import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

s, e = map(int, input().split())

# 시작점부터 i번째 도시까지의 최소비용 저장
INF = 10000000000
cost = [INF]*(N+1)
cost[s] = 0


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cur_cost, cur = heapq.heappop(q)

        # 이 조건문이 있어야 시간초과 해결됨!!
        # https://www.acmicpc.net/board/view/120269
        if cost[cur] < cur_cost:
            continue

        for ncost, to in graph[cur]:
            if cost[cur] + ncost < cost[to]:
                cost[to] = cost[cur] + ncost
                heapq.heappush(q, (cost[to], to))


dijkstra(s)
print(cost[e])