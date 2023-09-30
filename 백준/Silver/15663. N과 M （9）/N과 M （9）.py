import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

result = []
visited = [False] * N


def dfs():
    if len(result) == M:
        print(*result)
        return

    # 이전 항목(중복 수열인지 판단)
    pre = 0

    for i in range(N):
        if visited[i] or pre == nums[i]:
            continue

        visited[i] = True
        pre = nums[i]
        result.append(nums[i])
        dfs()
        visited[i] = False
        result.pop()


dfs()