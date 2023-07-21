import sys
import collections
input = sys.stdin.readline

def bf():
    for i in range(n):
        for j in range(len(edges)):
            cur, next, cost = edges[j]
            if dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == n - 1:
                    return True
    return False
                        
TC = int(input())

for _ in range(TC):
    n, m, w = map(int, input().split())
    edges = []
    dist = [1e9] * (n + 1)
    for i in range(m + w):
        s, e, t = map(int, input().split())
        if i >= m:
            t = -t
        else:
            edges.append((e, s, t))
        edges.append((s, e, t))
    if bf():
        print("YES")
    else:
        print("NO")