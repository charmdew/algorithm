import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

result = []


def dfs():
    global N, M

    if len(result) == M:
        print(*result)
        return

    for x in nums:
        if x in result:
            continue
        result.append(x)
        dfs()
        result.pop()


dfs()