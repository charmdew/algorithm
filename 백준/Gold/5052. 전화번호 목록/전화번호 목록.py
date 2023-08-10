import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())

    phone_nums = [input().rstrip() for _ in range(n)]
    phone_nums.sort(key=lambda x: len(x))

    prefix = dict()
    consistency = True

    for phone_num in phone_nums:
        # 다른 번호가 현재 번호의 접두어인지 확인
        for i in range(1, len(phone_num)+1):
            # 이미 있는 경우 일관성 유지 못함
            if phone_num[:i] in prefix:
                consistency = False
                break

        # 현재 전화번호 접두어로 추가
        prefix[phone_num[:i]] = 1

        if not consistency:
            break

    print("YES" if consistency else "NO")