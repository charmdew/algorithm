# DP 활용
# dp[i] : i(ci의 합)로 확보할 수 있는 최대 메모리 크기
import sys 

input = sys.stdin.readline 

N, M = map(int, input().split())

m = list(map(int, input().split()))
c = list(map(int, input().split()))
c_sum = sum(c)

# 1 ≤ N ≤ 100, 0 ≤ c1, ..., cN ≤ 100 이므로 ci의 합의 최댓값은 10000
dp = [0]*(c_sum+1)

for i in range(N):
    # 참고 : https://www.acmicpc.net/board/view/6667
    # 루프를 반대로 돌려야함!!
    # 증가하는 순으로 루프를 돌리면 m[i]가 여러번 더해짐
    for x in range(c_sum, c[i]-1, -1):
        dp[x] = max(dp[x], dp[x-c[i]]+m[i])

# 순서대로 확인하면서 M 이상인 경우 출력
for i in range(1, c_sum+1):
    if dp[i]>=M:
        print(i)
        break