array = [10, -3, -5, 2, 5]
min_value = array[0]
min_index = 0

for i in range(1, len(array)):
    if array[i] < min_value:
        min_value = array[i]
        min_index = i

print("Номер минимального элемента:", min_index)