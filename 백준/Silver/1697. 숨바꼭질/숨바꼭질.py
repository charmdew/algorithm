from collections import deque

INF = 100001

def bfs(N, K):
  l = int(max(N, K)*1.5)
  # 해당 위치로 이동하는데 걸리는 최단 시간 저장
  time = [INF]*(l+1)
  time[N] = 0  
  
  q = deque()
  q.append(N)
  
  while q:
    X = q.popleft()

    # 동생이 있는 위치
    if X == K:
      break

    # 걷기, 순간이동
    nx = [X-1, X+1, 2*X]
    for x in nx:
      # 범위 체크
      if x<0 or l<x:
        continue
      # 이미 방문한 곳이라면
      if time[x]<INF:
        continue
      
      time[x] = time[X]+1
      q.append(x)

  return time[K]

N, K = map(int, input().split())

# 동생이 수빈이보다 앞에 있거나 같은 위치이면
if K<=N:
  print(N-K)

# 동생이 수빈이보다 뒤에 있다면
else:
  print(bfs(N, K))