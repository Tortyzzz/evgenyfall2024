def f(n, m):
    if n > m:
        print('Number', m, ' < ', n)
    elif n < m:
        print('Number', m, ' > ', n)
    else:
        print('The numbers are equal')

a = int(input('Введите число n'))
b = int(input('Введите число m'))
print(f(a, b))