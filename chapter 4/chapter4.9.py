with open('D:\PyCharm Community Edition 2024.2\mainconfigjob\IBAN.py', 'r') as file:
    iban_lengths = {line.split()[0]: int(line.split()[1]) for line in file}

print(iban_lengths)


iban_lengths = dict(map(lambda line: (line.split()[0], int(line.split()[1])), open('D:\PyCharm Community Edition 2024.2\mainconfigjob\IBAN.py')))
print(iban_lengths)