r = int(input('Введите радиус окружности'))

d = r * 2
print('Диаметр окружности равен', d)

for i in range(1, 501):
    x = 0
    for j in range(r, 501):
        x = x + j

print('Сумма всех целых чисел', x)