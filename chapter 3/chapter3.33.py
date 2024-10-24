def double_factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1

    result = 1
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            result *= i
    else:
        for i in range(1, n + 1, 2):
            result *= i

    return result

n = int(input("Введите число n: "))
result = double_factorial(n)
if result is not None:
    print(f"{n}!! = {result}")
else:
    print("Двойной факториал не определен для отрицательных чисел.")