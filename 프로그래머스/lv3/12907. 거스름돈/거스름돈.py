"""
[풀이 참고함..]
거스름돈 n원을 줄 때 방법의 경우의 수 구하기
"""


def solution(n, money):
    answer = 0
    
    dp = [0] * (n+1)
    
    dp[0] = 1
    
    for m in money:
        for i in range(m, n+1):
            dp[i] += dp[i-m] % 1000000007
            
    answer = dp[n]
    
    return answer