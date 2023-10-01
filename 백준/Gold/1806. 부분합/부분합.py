import sys

input = sys.stdin.readline

N, S = map(int, input().split())

nums = list(map(int, input().split()))

s, e = 0, 1
# 부분합
subtotal = nums[0]
# 부분합 원소 개수
cnt = 1

# 부분합이 S이상이 되는 것 중 가장 짧은 것의 길이
result = 100001

while s < e:
    if subtotal >= S:
        result = min(result, cnt)
        subtotal -= nums[s]
        s += 1
        cnt -= 1
    else:
        # 부분합이 S보다 작은데 e가 N이상인 경우는 불가능!
        if e >= N:
            break
        subtotal += nums[e]
        e += 1
        cnt += 1

print(result if result < 100001 else 0)