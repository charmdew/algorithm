"""
[풀이 찾아봄]

- start = 0, end = 0으로 초기화합니다.
- start를 n까지 for문 순회합니다.
- start값부터 시작하여 처음 같은 숫자가 나올 때까지 end를 증가시킵니다.
- end가 더 이상 진전할 수 없다면, end - start를 결괏값에 더해줍니다.
    * 만약에 1, 2, 3, 4, 5라는 수열이라면, start가 0일 때 end는 5까지 진행됩니다. 
    * 따라서 1, 12, 123, 1234, 12345의 5개의 수열이 생성될 수 있기 때문에 end - start를 더해줍니다.
- 현재 start값에 대한 모든 판단이 끝났다면, start값에 대한 방문처리를 해제해줍니다.
- 다음 start값에 대해 3~5 반복

"""

import sys 

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

# 방문 여부 저장
visited = [False] * (N+1)

answer = 0

e = 0
for s in range(0, N):
    while e<N:
        if visited[nums[e]]:
            break
        visited[nums[e]] = True
        e += 1
    answer += (e-s)
    visited[nums[s]] = False

print(answer)