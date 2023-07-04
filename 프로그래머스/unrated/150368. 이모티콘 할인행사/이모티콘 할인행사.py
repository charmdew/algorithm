# 할인율은 10%, 20%, 30%, 40% 중 하나
rate = [10, 20, 30, 40]

# 이모티콘 플러스 서비스 가입자수
max_service = 0
# 이모티콘 판매액
max_amount = 0

def perm(cnt, sales, users, emoticons, N, K):
    global max_service, max_amount
    
    if cnt == K:
        # sales의 할인 비율을 적용했을 때 이모티콘 판매액, 가입자수 구하기
        total_price = 0
        total_service = 0
        for x in range(N):
            cost = 0
            for j, s in enumerate(sales):
                # 할인율이 사용자의 기준 비율보다 더 높다면
                if s >= users[x][0]:
                    # 이모티콘 구매
                    cost += emoticons[j]//100 * (100-s)
            # 일정 가격 이상의 돈을 사용하면 이모티콘 구매 모두 취소, 플러스 서비스 가입
            if cost >= users[x][1]:
                total_service += 1
            else:
                total_price += cost
        
        # 목표1. 가입자수 최대한 늘리기
        # 목표2. 판매액 최대한 늘리기
        
        # 가입자수가 많은 경우를 우선으로 저장
        if total_service > max_service:
            max_service = total_service
            max_amount = total_price
        # 가입자수가 같은 경우는 판매액을 최대한 늘리기
        elif total_service == max_service:
            max_amount = max(max_amount, total_price)
    
        return
    
    # 할인 비율로 가능한 모든 경우 (중복순열)
    for i in range(4):
        sales.append(rate[i])
        perm(cnt+1, sales, users, emoticons, N, K)
        sales.pop()

def solution(users, emoticons):
    answer = []

    perm(0, [], users, emoticons, len(users), len(emoticons))
    
    answer = [max_service, max_amount]
    
    return answer