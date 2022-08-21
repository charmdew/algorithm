import sys
input = sys.stdin.readline

from collections import deque

n, m ,v =map(int, input().split())

edge=[[] for _ in range(n+1)]
visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)

ord_dfs=[]
ord_bfs=[]

for _ in range(m):
  a, b = map(int, input().split())
  edge[a].append(b)
  edge[b].append(a)

for i in range(1, n+1):
  edge[i].sort()

def dfs(x):
  ord_dfs.append(x)
  for e in edge[x]:
    if visited_dfs[e]==False:
      visited_dfs[e]=True
      dfs(e)

def bfs(x):
  q= deque()
  q.append(edge[x])
  ord_bfs.append(x)
  
  while q:
    vv = q.popleft()
    for v in vv:
      if visited_bfs[v]==False:
        ord_bfs.append(v)
        visited_bfs[v] = True
        q.append(edge[v])

visited_dfs[v]=True
dfs(v)

visited_bfs[v]=True
bfs(v)

print(*ord_dfs)
print(*ord_bfs)