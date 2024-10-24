import os

exit_code = os.system('ls')

if exit_code == 0:
    print("Команда выполнена успешно.")
else:
    print(f"Команда завершилась с ошибкой. Код ошибки: {exit_code}")