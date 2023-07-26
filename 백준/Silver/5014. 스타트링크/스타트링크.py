# dfs를 사용하면 런타임에러(RecursioinError)가 뜬다
# bfs 사용하기!
# 81퍼센트에서 계속 틀렸는데 0층은 없다는 것을 간과함!!

import sys
from collections import deque

input = sys.stdin.readline

# 강호는 S층에서 G층으로 넘어가야함
F, S, G, U, D = map(int, input().split())

# 층 방문 여부
visited = [False] * (F+1)

# 눌러야하는 버튼 수의 최솟값
min_cnt = 1e9

q = deque()
q.append((S, 0))

while q:
    pos, cnt = q.popleft()

    # G층에 도달한 경우
    if pos == G:
        min_cnt = cnt

    if visited[pos]:
        continue
    visited[pos] = True

    # 버튼 2개만 존재
    # 위로 U층을 가는 경우
    if U != 0 and pos + U <= F and not visited[pos+U]:
        q.append((pos+U, cnt+1))
    # 아래로 D층을 가는 경우
    if D != 0 and pos - D > 0 and not visited[pos-D]:
        q.append((pos-D, cnt+1))


print(min_cnt if min_cnt < 1e9 else "use the stairs")