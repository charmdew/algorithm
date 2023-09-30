import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

result = []


def dfs(x):
    if len(result) == M:
        print(*result)
        return

    # 이전 항목(중복 수열인지 판단)
    pre = 0

    for i in range(x, N):
        if pre == nums[i]:
            continue

        pre = nums[i]
        result.append(nums[i])
        dfs(i)
        result.pop()


dfs(0)