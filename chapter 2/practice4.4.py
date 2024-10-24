def f(a, b):
    if b % a == 0:
        return 'а Является делителем b'
    else:
        return 'Не является делителем'
b = float(input('Введите делимое:'))
a = float(input('Введите делитель:'))
print(f"Результат вычислений: {f(a, b)}")