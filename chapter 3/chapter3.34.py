def turtle_movement(commands):
    # Начальные координаты и направление
    x, y = 0, 0
    direction = 0  # 0 - север, 1 - восток, 2 - юг, 3 - запад

    # Словарь для изменения координат в зависимости от направления
    direction_moves = {
        0: (0, 1),  # Север
        1: (1, 0),  # Восток
        2: (0, -1),  # Юг
        3: (-1, 0)  # Запад
    }

    # Список для хранения маршрута
    path = [(x, y)]

    for command in commands:
        if command == 'F':
            # Перемещение вперед
            dx, dy = direction_moves[direction]
            x += dx
            y += dy
            path.append((x, y))
        elif command == 'L':
            # Поворот влево
            direction = (direction - 1) % 4
        elif command == 'R':
            # Поворот вправо
            direction = (direction + 1) % 4
        elif command == 'S':
            # Остановка и выход
            break

    return path


# Пример использования
commands = input("Введите последовательность команд: ")
route = turtle_movement(commands)

# Вывод маршрута передвижения робота
print("Маршрут передвижения робота:")
for position in route:
    print(position)