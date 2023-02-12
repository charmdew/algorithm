#[23.01.29] 19:49~
from collections import Counter

def solution(weights):
    answer = 0
    
    count = Counter(weights)
    
    # 무게가 같은 경우 처리
    for k, v in count.items():
        if v > 1: 
            # v개 중 2개를 뽑는 경우의 수
            answer += v * (v-1) / 2
    
    weights = list(set(weights))
    
    # 배율 3/4, 2/3, 1/2 확인!
    check = (3/4, 2/3, 1/2)
    
    for w in weights:
        for c in check:
            if w*c in weights:
                answer += count[w] * count[w*c]
    
    return answer