import sys

input = sys.stdin.readline

# 벽장의 개수 N 입력 ( 3 < N <= 20 )
N = int(input())

# 열려있는 두개의 벽장을 나타내는 두 개의 정수
open1, open2 = map(int, input().split())


def solve(orderIdx, open1, open2):
    if orderIdx == M:
        return 0

    if dp[orderIdx][open1][open2] != -1:
        return dp[orderIdx][open1][open2]

    open1_cnt = solve(
        orderIdx+1, order[orderIdx], open2) + abs(order[orderIdx] - open1)
    open2_cnt = solve(orderIdx+1, open1,
                      order[orderIdx]) + abs(order[orderIdx] - open2)

    dp[orderIdx][open1][open2] = min(open1_cnt, open2_cnt)

    return dp[orderIdx][open1][open2]


order = []  # 열어야 하는 문 저장해둘 리스트
M = int(input())  # 열어야 하는 문 개수
for _ in range(M):
    order.append(int(input()))

# 3차원 dp 선언하기!
"""
    1. 열어야 하는 문들 중에 몇 번째로 열어야하는 문인지
    2. 열려있는 문 1
    3. 열려있는 문 2
"""
# 문에 직접 접근하는 인덱스는 +1 되어있어서 크기를 1씩 늘림
# M은 열어야 하는 문의 개수
dp = [[[-1]*(N+1) for _ in range(N+1)] for _ in range(M)]

print(solve(0, open1, open2))