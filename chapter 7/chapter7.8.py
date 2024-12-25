def ternary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Два средних индекса
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Средние элементы
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        # Определяем, в какой части продолжить поиск
        if target < arr[mid1]:
            right = mid1 - 1  # Ищем в первой части
        elif target > arr[mid2]:
            left = mid2 + 1  # Ищем в третьей части
        else:
            left = mid1 + 1  # Ищем во второй части
            right = mid2 - 1

    return -1  # Элемент не найден


# Пример использования
sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index_of_five = ternary_search(sorted_numbers, 5)
print(index_of_five)

index_of_ten = ternary_search(sorted_numbers, 10)
print(index_of_ten)

# Тесты
# Тест 1
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 4
# Тест 2
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == 2
# Тест 3
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 0
# Тест 4
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == -1
# Тест 5
assert ternary_search([], 1) == -1  # Пустой массив

print("Все тесты пройдены!")
