def tr(metres):
    kme = metres / 1000
    return kme
def f(kme, km):
    if kme < km:
        return 'Значение в метрах меньше на', km - tr(metres), 'км'
    elif kme > km:
        return 'Значение в километрах меньше на ', tr(metres) - km, 'км'
    else:
        return 'Значения равны'

metres = int(input("Введите значение в метрах: "))
km = int(input('Введите значение в километрах'))

print('Результат сравнения: ', f(tr(metres), km))



