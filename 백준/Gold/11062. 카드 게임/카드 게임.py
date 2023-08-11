"""
DP 활용
    
dp[i][j] : i~j의 카드가 있을 때 근우가 선택할 수 있는 최대 합
- 근우 / 명우 차례일 때 식을 나눠야 함!
    근우차례 : i~j 카드가 있을 때, 선택할 카드(i or j) 다음에 선택할 카드의 합이 최대가 되도록 선택
    명우차례 : i~j 카드가 있을 때, 명우의 선택(i or j) 후 남은 카드들로 근우가 선택할 카드의 합이 최소가 되도록 선택

"""

import sys
import heapq

input = sys.stdin.readline


for t in range(int(input())):
    N = int(input())

    cards = list(map(int, input().split()))

    dp = [[0]*N for _ in range(N)]

    # True일 때 근우차례
    turn = True if N % 2 == 1 else False

    for size in range(N):
        for i in range(N-size):
            if size == 0:
                dp[i][i+size] = cards[i] if turn else 0
                continue
            # 근우차례
            if turn:
                dp[i][i+size] = max(dp[i+1][i+size]+cards[i],
                                    dp[i][i+size-1] + cards[i+size])
            # 명우차례
            else:
                dp[i][i+size] = min(dp[i+1][i+size], dp[i][i+size-1])
        turn = not turn  # 차례 바꾸기

    print(dp[0][N-1])