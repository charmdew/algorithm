# 이분탐색을 사용해야 함!
# 원소값을 정해서 그 값이 (a~b) 번째 수임을 알아낸 뒤에 k가 이 구간에 포함되지 않으면
# 원소값을 늘리거나 줄여서 다시 수행하는 방식으로 답 찾기
# A보다 작은 숫자가 몇개인지 찾아내면 A가 몇번째 숫자인지 알 수 있음
#   i번째 행에 x보다 작거나 같은 숫자의 개수: x를 행으로 나눈 몫

import sys

sys = sys.stdin.readline

N = int(input())
K = int(input())

result = 0

s, e = 1, min(10**9, N**2)
while s <= e:
    mid = (s+e)//2

    cnt = 0  # mid보다 작거나 같은 숫자 개수
    for i in range(1, N+1):
        cnt += min(mid//i, N)

    if cnt >= K:
        result = mid
        e = mid - 1
    else:
        s = mid + 1

print(result)