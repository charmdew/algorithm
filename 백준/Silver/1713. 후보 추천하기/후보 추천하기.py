"""
1. 초기에 모든 사진틀 비어있음
2. 어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 사진틀에 게시됨
3. 비어있는 사진틀이 없는 경우
   - 추천 받은 횟수가 가장 적은 학생(두 명 이상일 경우 게시된지 가장 오래된)의 사진 삭제
   - 그 자리에 새롭게 추천받은 학생의 사진 게시
4. 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가
5. 사진들에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀜
"""

# 우선순위 큐를 이용하려고 했는데 추천 받은 횟수를 처리하기 번거로움
# 딕셔너리 사용! => key: 학생번호, value:(추천받은 횟수, 게시된 시간) 

import sys 

input = sys.stdin.readline 

N = int(input())
K = int(input())

frame = dict()

nums = list(map(int, input().split()))
for t in range(1, K+1):
    # 추천을 받은 학생 번호
    x = nums[t-1]

    # 추천 받은 학생이 사진틀에 이미 있다면
    if x in frame:
        cnt, time = frame[x]
        frame[x] = (cnt+1, time)

    # 추천 받은 학생이 사진틀에 없다면
    else:
        # 비어있는 틀이 있다면
        if len(frame) < N:
            frame[x] = (1, t)
        else:
            # 틀에서 하나 제거
            # 추천 받은 횟수가 가장 적은 학생(두 명 이상일 경우 게시된지 가장 오래된)
            sframe = sorted(frame.items(), key=lambda x:[x[1][0], x[1][1]])
            sframe.pop(0)

            frame = dict(sframe)

            # 현재 학생 추가
            frame[x] = (1, t)

print(*sorted(frame.keys()))