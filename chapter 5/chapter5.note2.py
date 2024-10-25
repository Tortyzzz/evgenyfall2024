import itertools

flowers_set1 = {"rose", "jasmine", "lily"}
flowers_set2 = {"orchid", "tulip", "violet", "daisy"}
flowers_set3 = {"lavender", "sunflower"}

combinations1 = list(itertools.product(flowers_set1))
combinations2 = list(itertools.product(flowers_set2))
combinations3 = list(itertools.product(flowers_set3))
combinations1 = len(combinations1)
combinations2 = len(combinations2)
combinations3 = len(combinations3)
sum = combinations1 + combinations2 + combinations3

print(f"Количество всех возможных букетов 1: {combinations1}, 2: {combinations2}, 3: {combinations3}")
print(f"Сумма всех букетов из разных наборов: {sum}")