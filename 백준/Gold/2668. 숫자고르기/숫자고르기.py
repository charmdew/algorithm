# 깊이 우선 탐색 이용

import sys

input = sys.stdin.readline

N = int(input())
nums = [0]+[int(input()) for _ in range(N)]

result = set()


def dfs(i, first, second):
    global N, result

    first.add(i)
    second.add(nums[i])

    if nums[i] in first:
        if first == second:
            result.update(first)
            return True
        return False
    return dfs(nums[i], first, second)


# dfs 실행
for i in range(1, N+1):
    if i not in result:
        dfs(i, set(), set())
# print(result)

print(len(result))
print(*sorted(list(result)), sep='\n')