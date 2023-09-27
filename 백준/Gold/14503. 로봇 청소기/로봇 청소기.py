import sys
input= sys.stdin.readline
from collections import deque

# 세로 크기 N, 가로 크기 M 입력 (3 ≤ N, M ≤ 50)
N, M = map(int, input().split()) 

# 로봇 청소기가 있는 칸 (r, c), 바라보는 방향 d 입력
r, c, d = map(int, input().split())

place = [list(map(int, input().split())) for _ in range(N)]

def bfs(r, c, dd, place):
  # 방향 (북, 동, 남, 서)
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]

  # 로봇 청소기 위치, 방향
  x, y, d = r, c, dd
  
  cnt = 0

  while True:
    if place[x][y]==0:
      # 현재 위치를 청소함
      place[x][y] = 2
      cnt += 1 # 영역 개수 +1

    # 왼쪽 방향
    nd = d-1 if d>0 else 3
    
    for i in range(4): 
      nx = x + dx[nd]
      ny = y + dy[nd]
      
      # 현재 위치 바로 왼쪽에 빈 공간이 존재한다면
      if place[nx][ny] == 0:
        # print("빈 공간", nx, ny, nd)
        x, y, d = nx, ny, nd
        break
      else:
        # 2a 단계가 연속으로 4번 실행된 경우    
        if i==3:
          # 바로 뒤쪽 확인
          nx = x + dx[(nd+2)%4]
          ny = y + dy[(nd+2)%4]
    
          # 바로 뒤쪽이 벽이라면 작동 멈춤
          if place[nx][ny]==1:
            # print("바로 뒤쪽 벽!", nx, ny, nd)
            return cnt
          else:
            # 한칸 후진
            # print("한칸 후진", nx, ny, nd)
            x, y, d = nx, ny, nd
        else:
          # 왼쪽 방향 회전
          nd = nd-1 if nd>0 else 3
        
  return cnt

print(bfs(r, c, d, place))
# for i in range(N):
#   print(*place[i])