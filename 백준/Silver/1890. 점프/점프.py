import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for i in range(N)]

dp =[[0]*N for i in range(N)]
dp[0][0] = 1

for i in range(N):
  for j in range(N):
    if i== N-1 and j==N-1:
      print(dp[i][j])
      break
      
    # 아래로 이동
    if i+board[i][j]<N:
      dp[i+board[i][j]][j] += dp[i][j]

    # 오른쪽 이동
    if j+board[i][j]<N:
      dp[i][j+board[i][j]] +=dp[i][j]