import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

result = []


def dfs(x):
    global N, M

    if len(result) == M:
        print(*result)
        return

    for i in range(x, N):
        result.append(nums[i])
        dfs(i)
        result.pop()


dfs(0)