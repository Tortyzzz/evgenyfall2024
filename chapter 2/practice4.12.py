def main():
    choice = input("Введите '1' для конвертации из килобайтов в байты или '2' для конвертации из байтов в килобайты: ")

    if choice == '1':
        kilobytes = float(input("Введите количество килобайт: "))
        bytes_result = kilobytes * 1024
        print(f"{kilobytes} КБ = {bytes_result} Б")

    elif choice == '2':
        bytes = float(input("Введите количество байт: "))
        kilobytes_result = bytes / 1024
        print(f"{bytes} Б = {kilobytes_result} КБ")

    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()