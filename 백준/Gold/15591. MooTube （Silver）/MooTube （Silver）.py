# 두 동영상이 서로 얼마나 가까운 지를 측정하는 단위 : USADO

import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append([q, r])
    graph[q].append([p, r])

INF = 1e9

# 모든 정점 사이의 USADO 구하기
usado = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    q = deque()
    q.append(i)  # 시작 동영상

    while q:
        e = q.popleft()

        for g in graph[e]:
            # g[0]: 연결된 동영상, g[1]: USADO 값
            if g[0] == i:  # 시작 동영상인 경우 넘어감
                continue

            # 방문하지 않았던 동영상인 경우
            if usado[i][g[0]] == INF:
                # USADO 중 최솟값 저장
                usado[i][g[0]] = min(g[1], usado[i][e])
                q.append(g[0])
    usado[i][i] = 0

for i in range(Q):
    k, v = map(int, input().split())

    answer = 0
    for j in range(1, N+1):
        if usado[v][j] >= k:
            answer += 1

    print(answer)