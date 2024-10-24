import sys
from sys import setrecursionlimit
setrecursionlimit(3_000)

def tet(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x ** tet(x, n - 1)

s = int(input())
s1 =int(input())

result_5_3 = tet(s, s1)

print(f"{s}^{s1} = {result_5_3}, количество цифр: {len(str(result_5_3))}")