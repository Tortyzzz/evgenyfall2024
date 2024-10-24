numbers = list(range(10))

user_input = int(input("Введите число для вывода таблицы умножения: "))

print("  ".join(str(num) for num in numbers))

for number in numbers:
    result = user_input * number
    print(result, end=" ")