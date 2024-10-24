def calculate_gc_content(sequence):

    sequence = sequence.upper()

    first_letter_count = sequence.count('G')
    second_letter_count = sequence.count('C')

    total_bases = len(sequence)

    if total_bases == 0:
        return 0, 0

    first_letter_percentage = (first_letter_count / total_bases) * 100
    second_letter_percentage = (second_letter_count / total_bases) * 100

    return first_letter_percentage, second_letter_percentage

sequence = str(input("Введите последовательность"))
first_letter = str(input('Первая буква для поиска'))
second_letter = str(input("Вторая буква для поиска"))

first_letter_percentage, second_letter_percentage = calculate_gc_content(sequence)
print(f"Процент G: {first_letter_percentage}%")
print(f"Процент C: {second_letter_percentage}%")