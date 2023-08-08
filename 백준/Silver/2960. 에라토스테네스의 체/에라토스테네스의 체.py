"""
[에라토스테네스의 체]
- N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘
1. 2부터 N까지 모든 정수를 적는다.
2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
3. P를 징고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
4. 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# 지웠는지 여부 저장
checked = [False]*(N+1)

# 지워진 수의 개수 구하기
cnt = 0

for x in range(2, N+1):
    # 아직 지우지 않은 수인 경우
    if not checked[x]:
        # x의 배수 확인
        mul = x
        while mul <= N:
            if not checked[mul]:
                cnt += 1

                # K번째 지워진 수라면 출력 후 종료
                if cnt == K:
                    print(mul)
                    break

                checked[mul] = True
            mul += x