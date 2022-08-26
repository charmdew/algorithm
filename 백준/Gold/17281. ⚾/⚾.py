# 이닝 수 : N(2 ≤ N ≤ 50)
N = int(input())

# 선수의 인덱스는 번호-1
numbers = [i for i in range(9)]

hitOrder = [-1]*9
isSelected = [False]*9
maxScore = 0        # 최대 득점 저장


# 이닝 점수 계산
def inning_score(order):
    # print(order)
    score = 0   # 득점
    hit_idx = 0  # 타석에 서는 타자 번호

    for inning in range(N):
        # print("[", inning+1, "이닝]", end=' ')
        r1, r2, r3 = 0, 0, 0
        out = 0  # 아웃된 타자 수

        # 들어온 타순으로 경기 진행
        while True:
            hitter = order[hit_idx]
            # print(hitter, end=' ')

            hit_idx = (hit_idx+1) % 9     # 다음 타자

            x = result[inning][hitter]
            # 아웃
            if x == 0:
                out += 1

                # 3명 아웃이면 이닝 종료
                if out == 3:
                    # print("아웃")
                    r1, r2, r3 = 0, 0, 0
                    break

            # 안타
            elif x == 1:
                score += r3
                r1, r2, r3 = 1, r1, r2

            elif x == 2:
                score += r2 + r3
                r1, r2, r3 = 0, 1, r1

            elif x == 3:
                score += r1 + r2 + r3
                r1, r2, r3 = 0, 0, 1

            # 홈런이면 roo에 있는 주자 + 현재 선수 1명 득점
            elif x == 4:
                score += r1+r2+r3 + 1
                # print("홈런!!")
                r1, r2, r3 = 0, 0, 0
    # print("이닝점수", score)
    return score


# 타순 정하기
def order_player(cnt):
    global maxScore
    if cnt == 9:
        # 1번 선수는 4번타자
        if hitOrder[3] != 0 : return
        maxScore = max(maxScore, inning_score(hitOrder))
        return

    for i in range(9):
        if isSelected[i]:
            continue

        isSelected[i] = True
        hitOrder[cnt] = numbers[i]
        order_player(cnt+1)
        isSelected[i] = False


result = []
for _ in range(N):
    # 각 이닝에서 얻는 결과(1번~N번)
    # 안타: 1, 2루타: 2, 3루타: 3, 홈런: 4, 아웃: 0
    result.append(list(map(int, input().split())))

order_player(0)
print(maxScore)

# for case in totalCase:
#     maxScore = max(maxScore, inning_score(case))
# print(maxScore)