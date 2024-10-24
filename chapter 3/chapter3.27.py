import math
def f(n, x = {}):
    if n <= 0:
        print("Введите положительное целое число.")
        return 0
    elif n == 1:
        print("Последовательность Фибоначчи:", 0)
        return 1
    elif n == 2:
        print("Последовательность Фибоначчи:", 0, 1)
        return 1
    elif n in x:
        return x[n]
    else:
        x[n] = f(n-1) + f(n-2)
        return  x[n]
    print("Последовательность Фибоначчи:", x)

n = int(input())

print(f(n, x = {}))


