def tr(metres):
    cent = metres * 100
    return cent
print('Enter a value in metres: ')
metres = int(input())
cent = tr(metres)
print('Distance in metres: ', metres, ' and centimetres', cent)