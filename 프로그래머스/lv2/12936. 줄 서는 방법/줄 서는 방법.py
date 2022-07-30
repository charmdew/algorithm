
def solution(n, k):
    answer = []
    l1 = [i for i in range(1, n+1)]
    
    # 팩토리얼 구하기
    fac = [1] * 20
    for i in range(2, 20):
        fac[i] = fac[i-1]*i;
    
    k -= 1
    
    for i in range(n, 0, -1):
        split_num = fac[n] // n
        answer.append(l1[k//split_num])
        l1.pop(k//split_num)
        k %= split_num
        n -= 1

    return answer