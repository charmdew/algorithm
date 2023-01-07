# 나머지 분배 법칙 & 지수 법칙 알아야 함
# 지수 법칙 : A^m+n = A^m x A^n
# 나머지 분배 법칙 : (AxB)%C = (A%C) *(B%C) % C

import sys

a, b, c = map(int, sys.stdin.readline().split())


def multi(a, n):
    if n == 1:
        return a % c
    else:
        tmp = multi(a, n // 2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c


print(multi(a, b))