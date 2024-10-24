def main():
    name = input("Введите ваше имя: ")

    age = int(input("Введите ваш возраст: "))

    current_year = 2024
    year_when_100 = current_year + (100 - age)

    message = f"Привет, {name}! Вам исполнится 100 лет в {year_when_100} году."
    print(message)


if __name__ == "__main__":
    main()