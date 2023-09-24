import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = []


def dfs(x, N, M):
    if len(nums) == M:
        print(*nums)
        return

    for i in range(x, N+1):
        nums.append(i)
        dfs(i, N, M)
        nums.pop()


dfs(1, N, M)