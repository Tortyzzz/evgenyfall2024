def find_quirky_numbers(digit_count):
    number = []

    for num in range( int('1' + '0' * digit_count) ):
        num1 = num
        numstr = str(num)

        while len(numstr) < digit_count:
            numstr = '0' + numstr

        num2 = int(numstr[:digit_count // 2])
        num3 = int(numstr[(digit_count // 2):])

        if num2 ** 2 + 2 *num2 * num3 + num3 ** 2 == num1:
            number.append(numstr)

    print(number)

    return number


# Тесты

# Тест 1
digit_count = 2
expected_output = ['00', '01', '81']
assert find_quirky_numbers(digit_count) == expected_output

# Тест 2
digit_count = 4
expected_output = ['0000', '0001', '0004', '0009', '0016', '0025',
                   '0040', '0081', '0096', '0160', '0250', '0400',
                   '0640', '0810', '1000', '1024', '1600', '2025',
                   '2500', '3025', '3600', '4000', '6400', '8100',
                   '9600']
assert find_quirky_numbers(digit_count) == expected_output

# Тест 3
digit_count = 6
expected_output = []  # Не ожидается никаких "причудливых" чисел
assert find_quirky_numbers(digit_count) == expected_output

# Тест 4
digit_count = 8
expected_output = []  # Не ожидается никаких "причудливых" чисел
assert find_quirky_numbers(digit_count) == expected_output

print("OK!")

